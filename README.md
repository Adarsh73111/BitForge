<div align="center">

# ⚡ BitForge
### The Coding Platform for Hardware Engineers
**Write Verilog & SystemVerilog. Simulate instantly. See waveforms live.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Next.js](https://img.shields.io/badge/Next.js-16.x-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org/)
[![Icarus Verilog](https://img.shields.io/badge/Icarus%20Verilog-12.0-orange)](http://iverilog.icarus.com/)

</div>

---

> BitForge is to hardware engineers what LeetCode is to software engineers.
> Practice RTL design and verification using Verilog and SystemVerilog,
> get instant simulation results, and visualize your circuit behavior
> through real waveforms — right in your browser.

---

## ✨ Features

- 🔌 **Verilog & SystemVerilog Support** — Write `.v` and `.sv` files directly in browser
- 🌊 **Live Waveform Visualizer** — See signal transitions after every submission
- 🤖 **AI Hint System** — Powered by Groq Llama 3.1 — 3 contextual hints per problem
- 📚 **30 Problems** — Combinational, Sequential, FSMs, ALUs, and more
- 🏷️ **Company Tags** — Problems tagged by Intel, Qualcomm, AMD, NVIDIA
- 🏆 **Leaderboard** — Rankings by problems solved
- 👤 **User Auth** — Register, login, logout with JWT
- 🔧 **Admin Panel** — Add, edit, test, delete problems with Monaco editors
- 📊 **Learning Tracks** — Structured paths for beginners to advanced
- 📖 **Documentation** — Built-in docs page

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js 16, TypeScript, Tailwind CSS, Monaco Editor |
| **Backend** | FastAPI (Python 3.11+) |
| **Database** | PostgreSQL (via SQLAlchemy + Alembic) |
| **Simulator** | Icarus Verilog (iverilog) |
| **AI Hints** | Groq API (Llama 3.1) |
| **Auth** | JWT tokens (python-jose) |
| **Hosting** | Vercel (frontend) + AWS EC2 (backend) |

---

## 🚀 Quick Start — Run Locally

### Prerequisites

Make sure you have these installed:

```bash
node --version      # 18+
python3 --version   # 3.11+
iverilog -V         # Icarus Verilog
psql --version      # PostgreSQL
```

#### Install Icarus Verilog

```bash
# Ubuntu/Debian
sudo apt-get install -y iverilog

# macOS
brew install icarus-verilog

# Windows (WSL recommended)
sudo apt-get install -y iverilog
```

#### Install PostgreSQL

```bash
# Ubuntu/Debian
sudo apt-get install -y postgresql postgresql-contrib
sudo systemctl start postgresql
sudo -u postgres psql -c "CREATE USER bitforge WITH PASSWORD 'bitforge';"
sudo -u postgres psql -c "CREATE DATABASE bitforge OWNER bitforge;"

# macOS
brew install postgresql
brew services start postgresql
psql postgres -c "CREATE USER bitforge WITH PASSWORD 'bitforge';"
psql postgres -c "CREATE DATABASE bitforge OWNER bitforge;"
```

---

## 📦 Option 1 — Clone & Run Manually

**Step 1 — Clone the Repository**

```bash
git clone https://github.com/Adarsh73111/BitForge.git
cd BitForge
```

**Step 2 — Backend Setup**

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
pip install bcrypt==4.0.1

# Create .env file
cp .env.example .env
```

Edit `.env` with your values:

```env
DATABASE_URL=postgresql://bitforge:bitforge@localhost:5432/bitforge
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your_secret_key_here_make_it_long
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=ap-south-1
S3_BUCKET=bitforge-waveforms
GROQ_API_KEY=your_groq_api_key
ENVIRONMENT=development
```

**Step 3 — Run Database Migrations**

```bash
cd backend
source venv/bin/activate
alembic upgrade head
python3 seed_all_problems.py
```

**Step 4 — Start Backend**

```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

- Backend running at: http://localhost:8000
- API Docs at: http://localhost:8000/docs

**Step 5 — Frontend Setup**

```bash
cd frontend
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

**Step 6 — Start Frontend**

```bash
cd frontend
npm run dev
```

Frontend running at: http://localhost:3000

---

## 🐳 Option 2 — Docker Compose (Recommended)

**Prerequisites:**
- Docker Desktop installed and running
- Docker Compose v2+

**Step 1 — Clone & Configure**

```bash
git clone https://github.com/Adarsh73111/BitForge.git
cd BitForge
cp .env.example .env
```

Edit `.env` with your API keys (`GROQ_API_KEY` is required for AI hints).

**Step 2 — Build & Run**

```bash
docker-compose up --build
```

This starts:
- Frontend on http://localhost:3000
- Backend on http://localhost:8000
- PostgreSQL on port 5432
- Redis on port 6379

**Step 3 — Seed the Database**

```bash
# In a new terminal
docker-compose exec backend python3 seed_all_problems.py
```

**Step 4 — Open BitForge**

Visit http://localhost:3000 🎉

```bash
# Stop everything
docker-compose down
```

---

## 🔧 Option 3 — GitHub Codespaces

The easiest way — no local setup needed!

1. Fork this repository
2. Click **Code → Codespaces → Create codespace on main**
3. Wait ~3 minutes for auto-setup
4. Run:

```bash
# Terminal 1 — Backend
cd backend && uvicorn app.main:app --reload --port 8000

# Terminal 2 — Frontend
cd frontend && npm run dev
```

Codespaces will prompt to open ports 3000 and 8000. Then seed problems:

```bash
cd backend && python3 seed_all_problems.py
```

---

## 🚀 Deploy to Production

### Frontend — Deploy to Vercel

```bash
npm install -g vercel
cd frontend
vercel --prod
```

Set environment variable in Vercel dashboard:
```
NEXT_PUBLIC_API_URL = https://your-backend-url.com
```

### Backend — Deploy to AWS EC2

```bash
# SSH into your EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Clone repo
git clone https://github.com/Adarsh73111/BitForge.git
cd BitForge/backend

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install bcrypt==4.0.1

# Configure .env
cp .env.example .env
nano .env  # Add your production values

# Run migrations & seed
alembic upgrade head
python3 seed_all_problems.py

# Create systemd service
sudo tee /etc/systemd/system/bitforge.service << 'EOF'
[Unit]
Description=BitForge FastAPI Backend
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/BitForge/backend
Environment="PATH=/home/ubuntu/BitForge/backend/venv/bin"
ExecStart=/home/ubuntu/BitForge/backend/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable bitforge
sudo systemctl start bitforge
```

---

## 📁 Project Structure

```
BitForge/
├── frontend/                  # Next.js application
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx       # Landing page
│   │   │   ├── problems/      # Problems list + solver
│   │   │   ├── login/         # Login page
│   │   │   ├── signup/        # Signup page
│   │   │   ├── leaderboard/   # Rankings
│   │   │   ├── tracks/        # Learning tracks
│   │   │   ├── docs/          # Documentation
│   │   │   ├── admin/         # Admin panel
│   │   │   └── profile/       # User profile
│   │   └── components/
│   │       ├── Navbar.tsx
│   │       ├── WaveformViewer.tsx
│   │       └── HintPanel.tsx
│   └── package.json
│
├── backend/                   # FastAPI application
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py        # JWT authentication
│   │   │   ├── problems.py    # Problem CRUD
│   │   │   ├── submissions.py # Code submission + simulation
│   │   │   ├── hints.py       # AI hints (Groq)
│   │   │   ├── users.py       # User profiles + leaderboard
│   │   │   └── admin.py       # Admin problem management
│   │   ├── core/
│   │   │   ├── config.py      # Settings
│   │   │   ├── database.py    # SQLAlchemy setup
│   │   │   └── security.py    # JWT + password hashing
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── problem.py
│   │   │   └── submission.py
│   │   └── services/
│   │       ├── simulator.py   # Icarus Verilog runner
│   │       ├── vcd_parser.py  # Waveform VCD parser
│   │       └── ai_hints.py    # Groq AI integration
│   ├── migrations/            # Alembic DB migrations
│   ├── seed_all_problems.py   # 30 problem seeder
│   └── requirements.txt
│
├── simulator/                 # Docker sandbox config
├── problems/                  # Problem definitions
├── docker-compose.yml
└── README.md
```

---

## 🔑 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `DATABASE_URL` | ✅ | PostgreSQL connection string |
| `SECRET_KEY` | ✅ | JWT signing key (make it long!) |
| `GROQ_API_KEY` | ✅ | Get free at [console.groq.com](https://console.groq.com) |
| `AWS_ACCESS_KEY_ID` | Optional | For S3 waveform storage |
| `AWS_SECRET_ACCESS_KEY` | Optional | For S3 waveform storage |
| `AWS_REGION` | Optional | Default: `ap-south-1` |
| `REDIS_URL` | Optional | For job queuing (future) |

---

## 🎮 Using BitForge

### Solving a Problem

1. Go to `/problems` and pick any problem
2. Read the description and truth table
3. Write your Verilog solution in the Monaco editor
4. Click **Submit**
5. See pass/fail result + live waveform visualization
6. Stuck? Use **AI Hints** (3 per problem)

### Admin Panel

Access at `/admin` using your `SECRET_KEY` as password. You can:

- ✅ Create new problems with Monaco editors
- ✅ Test problems before publishing
- ✅ Edit existing problems
- ✅ Delete problems

### Example Solution (AND Gate)

```verilog
module and_gate(
    input  wire a,
    input  wire b,
    output wire y
);
    assign y = a & b;
endmodule
```

---

## 🐛 Troubleshooting

**`iverilog` not found**

```bash
sudo apt-get install -y iverilog
which iverilog
iverilog -V
```

**Database connection failed**

```bash
sudo systemctl status postgresql
psql postgresql://bitforge:bitforge@localhost:5432/bitforge -c "\dt"
```

**Frontend can't reach backend**

```bash
cat frontend/.env.local
# Should show: NEXT_PUBLIC_API_URL=http://localhost:8000
curl http://localhost:8000/health
```

**bcrypt version error**

```bash
pip install bcrypt==4.0.1 --force-reinstall
```

**Migrations failed**

```bash
cd backend
source venv/bin/activate
alembic upgrade head
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Adding New Problems

Use the Admin Panel at `/admin` or add directly to `seed_all_problems.py`:

```python
{
  "title": "Your Problem Title",
  "slug": "your-problem-slug",
  "difficulty": "easy",          # easy / medium / hard
  "category": "combinational",   # combinational / sequential / verification
  "description": "## Problem\n\nDescription here...",
  "starter_code": "module your_module(\n    // ports\n);\n    // solution here\nendmodule",
  "testbench": "module tb;\n    // testbench code\nendmodule",
  "hints": ["Hint 1", "Hint 2"],
  "company_tags": ["Intel", "AMD"],
}
```

---

## 📊 Problem Categories

| Category | Count | Description |
|---|---|---|
| Combinational | 14 | Gates, Adders, Muxes, Decoders, ALU |
| Sequential | 12 | Flip-flops, Counters, FSMs, Shift Registers |
| Advanced | 4 | LFSR, PWM, Debounce, Ripple Carry |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- [Icarus Verilog](http://iverilog.icarus.com/) — Open source Verilog simulator
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) — VS Code editor in browser
- [Groq](https://groq.com/) — Ultra-fast AI inference for hints
- [FastAPI](https://fastapi.tiangolo.com/) — Modern Python web framework
- [Next.js](https://nextjs.org/) — React framework for production

---

<div align="center">
Built with ❤️ for hardware engineers
</div>
