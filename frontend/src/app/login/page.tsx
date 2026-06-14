"use client";
import { useState } from "react";
import Navbar from "@/components/Navbar";
import Link from "next/link";
import { Zap, Loader2 } from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function LoginPage() {
  const [form, setForm]       = useState({ username: "", password: "" });
  const [loading, setLoading] = useState(false);
  const [msg, setMsg]         = useState("");

  const handleLogin = async () => {
    setLoading(true); setMsg("");
    try {
      const body = new URLSearchParams();
      body.append("username", form.username);
      body.append("password", form.password);
      const res = await fetch(`${API}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body,
      });
      const data = await res.json();
      if (res.ok) {
        localStorage.setItem("token", data.access_token);
        setMsg("✅ Login successful! Redirecting...");
        setTimeout(() => window.location.href = "/problems", 1000);
      } else {
        setMsg("❌ " + (data.detail || "Invalid credentials"));
      }
    } catch {
      setMsg("❌ Connection error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{
        maxWidth: 400, margin: "80px auto", padding: 24,
        background: "var(--bg-surface)",
        border: "1px solid var(--border)", borderRadius: 16,
      }}>
        <div style={{ textAlign: "center", marginBottom: 32 }}>
          <div style={{
            width: 48, height: 48, borderRadius: 12,
            background: "var(--accent-dim)",
            border: "1px solid var(--accent)",
            display: "flex", alignItems: "center",
            justifyContent: "center", margin: "0 auto 16px",
          }}>
            <Zap size={24} color="var(--accent)" />
          </div>
          <h1 style={{ fontSize: 24, fontWeight: 700 }}>Welcome back</h1>
          <p style={{ color: "var(--text-muted)", fontSize: 14, marginTop: 4 }}>
            Log in to BitForge
          </p>
        </div>

        {["username", "password"].map(field => (
          <div key={field} style={{ marginBottom: 16 }}>
            <label style={{ fontSize: 13, color: "var(--text-muted)",
              display: "block", marginBottom: 6, textTransform: "capitalize" }}>
              {field}
            </label>
            <input
              type={field === "password" ? "password" : "text"}
              value={(form as any)[field]}
              onChange={e => setForm(f => ({...f, [field]: e.target.value}))}
              onKeyDown={e => e.key === "Enter" && handleLogin()}
              style={{
                width: "100%", padding: "10px 14px",
                background: "var(--bg-elevated)",
                border: "1px solid var(--border)",
                color: "var(--text-primary)",
                borderRadius: 8, fontSize: 14,
                boxSizing: "border-box" as any,
              }}
            />
          </div>
        ))}

        {msg && <p style={{ fontSize: 13, marginBottom: 12,
          color: msg.startsWith("✅") ? "var(--accent)" : "#ff4d6a" }}>{msg}</p>}

        <button onClick={handleLogin} disabled={loading} style={{
          width: "100%", background: "var(--accent)",
          color: "#0a0a0f", border: "none", cursor: "pointer",
          fontWeight: 700, fontSize: 15, padding: "12px",
          borderRadius: 8, marginBottom: 16,
          display: "flex", alignItems: "center",
          justifyContent: "center", gap: 8,
        }}>
          {loading ? <><Loader2 size={16} /> Logging in...</> : "Log in"}
        </button>

        <p style={{ textAlign: "center", fontSize: 13, color: "var(--text-muted)" }}>
          Don't have an account?{" "}
          <Link href="/signup" style={{ color: "var(--accent)", textDecoration: "none" }}>
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
}
