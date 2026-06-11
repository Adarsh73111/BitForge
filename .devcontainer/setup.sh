#!/bin/bash
echo "🔧 Setting up BitForge development environment..."

# Install Icarus Verilog (the HDL simulator)
sudo apt-get update -qq
sudo apt-get install -y iverilog gtkwave

# Verify iverilog installed
echo "✅ Icarus Verilog version: $(iverilog -V 2>&1 | head -1)"

# Install Python backend dependencies
cd /workspaces/bitforge/backend 2>/dev/null || true
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary \
    python-jose[cryptography] passlib[bcrypt] celery redis \
    python-dotenv pydantic-settings --quiet
echo "✅ Python packages installed"

# Install Node frontend dependencies (if package.json exists)
if [ -f /workspaces/bitforge/frontend/package.json ]; then
  cd /workspaces/bitforge/frontend
  npm install --silent
  echo "✅ Node packages installed"
fi

echo ""
echo "🎉 BitForge environment ready!"
echo "   Run: docker-compose up   → starts everything"
echo "   Frontend → http://localhost:3000"
echo "   Backend  → http://localhost:8000"
echo "   API Docs → http://localhost:8000/docs"
