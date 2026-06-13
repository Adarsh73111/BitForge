#!/usr/bin/env python3
"""
BitForge Simulator — runs Verilog/SystemVerilog code
using Icarus Verilog in a sandboxed environment.
"""
import subprocess
import tempfile
import os
import json
import sys
import signal
import time

TIMEOUT_SECONDS = 10
MAX_OUTPUT_LINES = 100

def run_simulation(user_code: str, testbench: str, language: str = "verilog") -> dict:
    """
    Compile and simulate user HDL code against hidden testbench.
    Returns result dict with status, output, and vcd path.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        # File extensions
        ext = ".sv" if language == "systemverilog" else ".v"

        # Write user design file
        design_file = os.path.join(tmpdir, f"design{ext}")
        with open(design_file, "w") as f:
            f.write(user_code)

        # Write testbench file
        tb_file = os.path.join(tmpdir, f"testbench{ext}")
        with open(tb_file, "w") as f:
            f.write(testbench)

        # Output files
        compiled_out = os.path.join(tmpdir, "simulation.out")
        vcd_file     = os.path.join(tmpdir, "waveform.vcd")

        # Step 1 — Compile with iverilog
        compile_cmd = [
            "iverilog",
            "-o", compiled_out,
            "-g2012",          # SystemVerilog 2012 support
            tb_file,
            design_file,
        ]

        try:
            compile_result = subprocess.run(
                compile_cmd,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                cwd=tmpdir,
            )
        except subprocess.TimeoutExpired:
            return {
                "status": "error",
                "output": "Compilation timed out",
                "vcd": None,
                "runtime_ms": None,
            }

        # Compilation failed
        if compile_result.returncode != 0:
            return {
                "status": "error",
                "output": compile_result.stderr[:2000],
                "vcd": None,
                "runtime_ms": None,
            }

        # Step 2 — Run simulation with vvp
        start_time = time.time()
        try:
            sim_result = subprocess.run(
                ["vvp", compiled_out],
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                cwd=tmpdir,
            )
        except subprocess.TimeoutExpired:
            return {
                "status": "error",
                "output": "Simulation timed out — check for infinite loops",
                "vcd": None,
                "runtime_ms": None,
            }

        runtime_ms = int((time.time() - start_time) * 1000)
        output = sim_result.stdout[:5000]

        # Step 3 — Read VCD waveform if generated
        vcd_data = None
        if os.path.exists(vcd_file):
            with open(vcd_file, "r") as f:
                vcd_data = f.read()[:50000]  # limit size

        # Step 4 — Determine pass/fail from output
        output_lower = output.lower()
        if "failed" in output_lower or "error" in output_lower or sim_result.returncode != 0:
            status = "failed"
        elif "passed" in output_lower or "all tests" in output_lower or "success" in output_lower:
            status = "passed"
        else:
            status = "passed"  # compiled and ran without errors

        return {
            "status": status,
            "output": output,
            "vcd": vcd_data,
            "runtime_ms": runtime_ms,
        }


if __name__ == "__main__":
    # Read input from stdin (JSON)
    input_data = json.loads(sys.stdin.read())

    result = run_simulation(
        user_code=input_data["user_code"],
        testbench=input_data["testbench"],
        language=input_data.get("language", "verilog"),
    )

    print(json.dumps(result))
