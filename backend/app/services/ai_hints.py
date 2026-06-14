"""
BitForge AI Hint System
Uses Groq (Llama 3) to give intelligent hints when users are stuck
"""
import httpx
from app.core.config import settings

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = """You are BitForge's AI assistant for hardware engineering education.
You help students learn Verilog and SystemVerilog by giving helpful hints — NOT full solutions.

Rules:
1. Never give the complete solution code
2. Give directional hints that guide thinking
3. Explain WHY something is wrong, not just what
4. Use hardware engineering terminology correctly
5. Keep responses concise — max 100 words
6. If the code has a syntax error, point to the specific issue
7. Be encouraging and supportive

You are an expert in:
- Verilog RTL design (combinational and sequential)
- SystemVerilog verification
- Digital logic — FSMs, pipelines, interfaces
- Common beginner mistakes in HDL"""

async def get_ai_hint(
    problem_title: str,
    problem_description: str,
    user_code: str,
    error_output: str,
    hint_number: int = 1,
) -> str:
    if not settings.GROQ_API_KEY:
        return "AI hints are not configured. Please add your Groq API key."

    hint_style = {
        1: "Give a very gentle nudge — just point them in the right direction without specifics",
        2: "Give a more specific hint about what concept or Verilog operator to use",
        3: "Give a direct hint about the exact approach needed, but still not the full solution",
    }.get(hint_number, "Give a helpful hint")

    user_message = f"""Problem: {problem_title}

Description summary:
{problem_description[:400]}

Student's current Verilog code:
```verilog
{user_code}
```

Simulation output / Error:
{error_output or "Student hasn't submitted yet"}

Hint level: {hint_number}/3
Style: {hint_style}

Give a helpful hint to guide this student learning Verilog."""

    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
        "Content-Type":  "application/json",
    }

    body = {
        "model":       "llama-3.1-8b-instant",
        "max_tokens":  200,
        "temperature": 0.7,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message},
        ],
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(GROQ_API_URL, headers=headers, json=body)
            data = response.json()
            if response.status_code == 200:
                return data["choices"][0]["message"]["content"]
            else:
                return f"AI hint unavailable: {data.get('error', {}).get('message', 'Unknown error')}"
    except Exception as e:
        return f"AI hint service error: {str(e)}"
