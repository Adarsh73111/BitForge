"use client";
import { useState } from "react";
import Navbar from "@/components/Navbar";
import Link from "next/link";
import { Zap, Loader2 } from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function SignupPage() {
  const [form, setForm]       = useState({ username: "", email: "", password: "" });
  const [loading, setLoading] = useState(false);
  const [msg, setMsg]         = useState("");

  const handleSignup = async () => {
    setLoading(true); setMsg("");
    try {
      const res = await fetch(`${API}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      const data = await res.json();
      if (res.ok) {
        setMsg("✅ Account created! Redirecting to login...");
        setTimeout(() => window.location.href = "/login", 1500);
      } else {
        setMsg("❌ " + (data.detail || "Registration failed"));
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
          <h1 style={{ fontSize: 24, fontWeight: 700 }}>Create account</h1>
          <p style={{ color: "var(--text-muted)", fontSize: 14, marginTop: 4 }}>
            Join BitForge — free forever
          </p>
        </div>

        {[
          { field: "username", type: "text" },
          { field: "email", type: "email" },
          { field: "password", type: "password" },
        ].map(({ field, type }) => (
          <div key={field} style={{ marginBottom: 16 }}>
            <label style={{ fontSize: 13, color: "var(--text-muted)",
              display: "block", marginBottom: 6, textTransform: "capitalize" }}>
              {field}
            </label>
            <input
              type={type}
              value={(form as any)[field]}
              onChange={e => setForm(f => ({...f, [field]: e.target.value}))}
              onKeyDown={e => e.key === "Enter" && handleSignup()}
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

        <button onClick={handleSignup} disabled={loading} style={{
          width: "100%", background: "var(--accent)",
          color: "#0a0a0f", border: "none", cursor: "pointer",
          fontWeight: 700, fontSize: 15, padding: "12px",
          borderRadius: 8, marginBottom: 16,
          display: "flex", alignItems: "center",
          justifyContent: "center", gap: 8,
        }}>
          {loading ? <><Loader2 size={16} /> Creating account...</> : "Sign up free"}
        </button>

        <p style={{ textAlign: "center", fontSize: 13, color: "var(--text-muted)" }}>
          Already have an account?{" "}
          <Link href="/login" style={{ color: "var(--accent)", textDecoration: "none" }}>
            Log in
          </Link>
        </p>
      </div>
    </div>
  );
}
