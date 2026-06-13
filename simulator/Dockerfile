FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Icarus Verilog + Python
RUN apt-get update && apt-get install -y \
    iverilog \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create simulation workspace
RUN mkdir -p /tmp/sims

# Copy simulation runner script
COPY scripts/run_simulation.py /usr/local/bin/run_simulation.py
RUN chmod +x /usr/local/bin/run_simulation.py

WORKDIR /tmp/sims

CMD ["python3", "/usr/local/bin/run_simulation.py"]
