# ⚡ BitForge

> The coding platform for hardware engineers. Write, simulate, and verify
> Verilog & SystemVerilog circuits in your browser — with instant waveform feedback.

## What is BitForge?

BitForge is to hardware engineers what LeetCode is to software engineers.
Practice RTL design and verification using Verilog and SystemVerilog,
get instant simulation results, and visualize your circuit behavior through
real waveforms.

## Supported Languages

| Language | Use Case |
|---|---|
| Verilog (.v) | RTL Design — combinational & sequential circuits |
| SystemVerilog (.sv) | Advanced design + verification, assertions, testbenches |

## Problem Categories

- Combinational Logic (gates, adders, muxes)
- Sequential Logic (flip-flops, counters, FSMs)
- Pipelined Designs
- Interface Design (UART, SPI, I2C)
- Verification (SystemVerilog assertions, testbenches)

## Tech Stack

- **Frontend**: Next.js + TypeScript + Tailwind CSS + Monaco Editor
- **Backend**: FastAPI (Python)
- **Simulator**: Icarus Verilog in Docker sandbox
- **Database**: PostgreSQL
- **Queue**: Redis + Celery
- **Hosting**: Vercel (frontend) + AWS (backend)

## Getting Started (Development)

```bash
git clone https://github.com/yourusername/bitforge
cd bitforge
cp .env.example .env
docker-compose up
```

- Frontend: http://localhost:3000
- Backend:  http://localhost:8000
- API Docs: http://localhost:8000/docs

## License

MIT — see LICENSE file
