"""
BitForge VCD Parser
Converts raw VCD (Value Change Dump) data into
clean JSON that the frontend waveform viewer can render.
"""
import re
from typing import Optional

def parse_vcd(vcd_data: str) -> dict:
    """
    Parse VCD file content into structured JSON.
    Returns signals with their time-value pairs.
    """
    if not vcd_data:
        return {"signals": [], "timescale": "1s", "duration": 0}

    signals    = {}   # symbol → {name, type, width, changes}
    scope      = []
    timescale  = "1s"
    current_time = 0
    in_dumpvars  = False

    lines = vcd_data.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Timescale
        if line.startswith("$timescale"):
            continue
        if "s" in line and "$end" not in line and len(line) < 20:
            timescale = line.strip()
            continue

        # Scope tracking
        if line.startswith("$scope"):
            parts = line.split()
            if len(parts) >= 3:
                scope.append(parts[2])
            continue

        if line.startswith("$upscope"):
            if scope:
                scope.pop()
            continue

        # Variable declarations
        if line.startswith("$var"):
            parts = line.split()
            if len(parts) >= 5:
                var_type   = parts[1]
                var_width  = int(parts[2])
                var_symbol = parts[3]
                var_name   = parts[4]
                full_name  = ".".join(scope + [var_name]) if scope else var_name
                if var_symbol not in signals:
                    signals[var_symbol] = {
                        "name":    var_name,
                        "full_name": full_name,
                        "type":    var_type,
                        "width":   var_width,
                        "changes": [],
                    }
            continue

        # Time markers
        if line.startswith("#"):
            try:
                current_time = int(line[1:])
            except ValueError:
                pass
            continue

        # Value changes — scalar (e.g. "0!" or "1#")
        if len(line) >= 2 and line[0] in "01xzXZ" and not line.startswith("$"):
            value  = line[0]
            symbol = line[1:]
            if symbol in signals:
                signals[symbol]["changes"].append({
                    "time":  current_time,
                    "value": value,
                })
            continue

        # Value changes — vector (e.g. "b1010 $")
        if line.startswith("b") or line.startswith("B"):
            parts = line.split()
            if len(parts) >= 2:
                value  = parts[0][1:]
                symbol = parts[1]
                if symbol in signals:
                    signals[symbol]["changes"].append({
                        "time":  current_time,
                        "value": value,
                    })
            continue

    # Calculate max time
    max_time = 0
    for sig in signals.values():
        if sig["changes"]:
            max_time = max(max_time, sig["changes"][-1]["time"])

    # Filter out internal/tb signals, keep top-level interesting ones
    filtered = {}
    for sym, sig in signals.items():
        name = sig["name"]
        # Skip integer counters and internal signals
        if sig["type"] == "integer":
            continue
        if sig["changes"]:
            filtered[sym] = sig

    return {
        "signals":   list(filtered.values()),
        "timescale": timescale,
        "duration":  max_time,
    }
