"""
BitForge Simulator Service
Runs Verilog/SystemVerilog code using Icarus Verilog
"""
import subprocess
import tempfile
import os
import json
import time

TIMEOUT_SECONDS = 15

def run_simulation(user_code: str, testbench: str, language: str = "verilog") -> dict:
    """
    Directly runs simulation using iverilog on the backend server.
    In production this will be moved to isolated Docker containers.
    """
    ext = ".sv" if language == "systemverilog" else ".v"

    with tempfile.TemporaryDirectory() as tmpdir:
        # Write files
        design_file  = os.path.join(tmpdir, f"design{ext}")
        tb_file      = os.path.join(tmpdir, f"testbench{ext}")
        compiled_out = os.path.join(tmpdir, "sim.out")
        vcd_file     = os.path.join(tmpdir, "waveform.vcd")

        with open(design_file, "w") as f:
            f.write(user_code)
        with open(tb_file, "w") as f:
            f.write(testbench)

        # Compile
        compile_result = subprocess.run(
            ["/usr/bin/iverilog", "-o", compiled_out, "-g2012", tb_file, design_file],
            capture_output=True, text=True,
            timeout=TIMEOUT_SECONDS, cwd=tmpdir,
        )

        if compile_result.returncode != 0:
            return {
                "status": "error",
                "output": compile_result.stderr[:2000],
                "vcd": None,
                "runtime_ms": None,
            }

        # Run
        start = time.time()
        sim_result = subprocess.run(
            ["/usr/bin/vvp", compiled_out],
            capture_output=True, text=True,
            timeout=TIMEOUT_SECONDS, cwd=tmpdir,
        )
        runtime_ms = int((time.time() - start) * 1000)

        output = sim_result.stdout[:5000]

        # Read VCD
        vcd_data = None
        if os.path.exists(vcd_file):
            with open(vcd_file, "r") as f:
                vcd_data = f.read()[:50000]

        # Determine status
        out_lower = output.lower()
        if "failed" in out_lower or sim_result.returncode != 0:
            status = "failed"
        else:
            status = "passed"

        return {
            "status": status,
            "output": output,
            "vcd": vcd_data,
            "runtime_ms": runtime_ms,
        }
