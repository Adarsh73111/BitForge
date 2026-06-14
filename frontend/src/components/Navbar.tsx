"use client";
import Link from "next/link";
import { useState, useEffect } from "react";
import { Menu, X, Zap, LogOut, User } from "lucide-react";

export default function Navbar() {
  const [open,     setOpen]     = useState(false);
  const [username, setUsername] = useState<string | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    const user  = localStorage.getItem("username");
    if (token && user) setUsername(user);
  }, []);

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    setUsername(null);
    window.location.href = "/";
  };

  return (
    <nav style={{
      background: "rgba(10,10,15,0.85)",
      backdropFilter: "blur(12px)",
      borderBottom: "1px solid var(--border)",
      position: "sticky", top: 0, zIndex: 100,
    }}>
      <div style={{
        maxWidth: 1200, margin: "0 auto",
        padding: "0 24px", height: 60,
        display: "flex", alignItems: "center",
        justifyContent: "space-between",
      }}>

        {/* Logo */}
        <Link href="/" style={{
          display: "flex", alignItems: "center",
          gap: 8, textDecoration: "none",
        }}>
          <div style={{
            width: 32, height: 32, borderRadius: 8,
            background: "var(--accent-dim)",
            border: "1px solid var(--accent)",
            display: "flex", alignItems: "center",
            justifyContent: "center",
          }}>
            <Zap size={16} color="var(--accent)" />
          </div>
          <span style={{
            fontFamily: "var(--font-mono)",
            fontWeight: 600, fontSize: 18,
            color: "var(--text-primary)",
          }}>
            Bit<span style={{ color: "var(--accent)" }}>Forge</span>
          </span>
        </Link>

        {/* Desktop Nav */}
        <div style={{ display: "flex", alignItems: "center", gap: 32 }}>
          {["Problems", "Tracks", "Leaderboard", "Docs"].map(item => (
            <Link key={item} href={`/${item.toLowerCase()}`} style={{
              color: "var(--text-muted)", textDecoration: "none",
              fontSize: 14, fontWeight: 500,
              transition: "color 0.2s",
            }}
              onMouseEnter={e => (e.currentTarget.style.color = "var(--text-primary)")}
              onMouseLeave={e => (e.currentTarget.style.color = "var(--text-muted)")}
            >{item}</Link>
          ))}
        </div>

        {/* Auth Buttons */}
        <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
          {username ? (
            <>
              <Link href="/profile" style={{
                display: "flex", alignItems: "center", gap: 6,
                color: "var(--text-muted)", textDecoration: "none",
                fontSize: 14, fontWeight: 500,
              }}>
                <User size={14} />
                {username}
              </Link>
              <button onClick={logout} style={{
                background: "var(--bg-elevated)",
                border: "1px solid var(--border)",
                color: "var(--text-muted)",
                cursor: "pointer", fontSize: 13,
                padding: "6px 14px", borderRadius: 6,
                display: "flex", alignItems: "center", gap: 6,
              }}>
                <LogOut size={13} /> Logout
              </button>
            </>
          ) : (
            <>
              <Link href="/login" style={{
                color: "var(--text-muted)", textDecoration: "none",
                fontSize: 14, fontWeight: 500, padding: "6px 16px",
              }}>Log in</Link>
              <Link href="/signup" style={{
                background: "var(--accent)", color: "#0a0a0f",
                textDecoration: "none", fontSize: 14, fontWeight: 600,
                padding: "6px 16px", borderRadius: 6,
              }}>Sign up</Link>
            </>
          )}
        </div>

        {/* Mobile */}
        <button onClick={() => setOpen(!open)} style={{
          background: "none", border: "none",
          cursor: "pointer", color: "var(--text-primary)",
          display: "none",
        }}>
          {open ? <X size={20} /> : <Menu size={20} />}
        </button>
      </div>

      {open && (
        <div style={{
          borderTop: "1px solid var(--border)",
          padding: "16px 24px",
          display: "flex", flexDirection: "column", gap: 16,
        }}>
          {["Problems", "Tracks", "Leaderboard", "Docs"].map(item => (
            <Link key={item} href={`/${item.toLowerCase()}`}
              style={{ color: "var(--text-muted)",
                textDecoration: "none", fontSize: 15 }}
              onClick={() => setOpen(false)}
            >{item}</Link>
          ))}
          <hr style={{ border: "none", borderTop: "1px solid var(--border)" }} />
          {username ? (
            <button onClick={logout} style={{
              background: "none", border: "none",
              color: "#ff4d6a", cursor: "pointer",
              fontSize: 15, textAlign: "left", padding: 0,
            }}>Logout</button>
          ) : (
            <>
              <Link href="/login" style={{ color: "var(--text-muted)",
                textDecoration: "none", fontSize: 15 }}>Log in</Link>
              <Link href="/signup" style={{ color: "var(--accent)",
                textDecoration: "none", fontSize: 15,
                fontWeight: 600 }}>Sign up</Link>
            </>
          )}
        </div>
      )}
    </nav>
  );
}
