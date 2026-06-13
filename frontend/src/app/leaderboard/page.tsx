"use client";
import { useState, useEffect } from "react";
import Navbar from "@/components/Navbar";
import { Trophy, Medal } from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function LeaderboardPage() {
  const [users, setUsers]   = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/users/`)
      .then(r => r.json())
      .then(data => { setUsers(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const rankColor = (i: number) => {
    if (i === 0) return "#FFD700";
    if (i === 1) return "#C0C0C0";
    if (i === 2) return "#CD7F32";
    return "var(--text-muted)";
  };

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{ maxWidth: 800, margin: "0 auto", padding: "48px 24px" }}>

        <div style={{ textAlign: "center", marginBottom: 48 }}>
          <Trophy size={40} color="var(--accent)" style={{ marginBottom: 16 }} />
          <h1 style={{ fontSize: 32, fontWeight: 700, marginBottom: 8 }}>Leaderboard</h1>
          <p style={{ color: "var(--text-muted)" }}>
            Top hardware engineers on BitForge
          </p>
        </div>

        {loading ? (
          <div style={{ textAlign: "center", color: "var(--text-muted)" }}>
            Loading...
          </div>
        ) : users.length === 0 ? (
          <div style={{
            textAlign: "center", color: "var(--text-muted)",
            background: "var(--bg-surface)",
            border: "1px solid var(--border)",
            borderRadius: 12, padding: 48,
          }}>
            No users yet — be the first to solve problems!
          </div>
        ) : (
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {users.map((user, i) => (
              <div key={user.username} style={{
                display: "flex", alignItems: "center", gap: 16,
                background: i < 3 ? "var(--bg-surface)" : "var(--bg-base)",
                border: `1px solid ${i < 3 ? rankColor(i) + "44" : "var(--border)"}`,
                borderRadius: 10, padding: "16px 20px",
              }}>
                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 18,
                  fontWeight: 700, color: rankColor(i), width: 32,
                  textAlign: "center",
                }}>
                  {i < 3 ? ["🥇","🥈","🥉"][i] : `${i+1}`}
                </span>
                <span style={{ flex: 1, fontWeight: 500, fontSize: 16 }}>
                  {user.username}
                </span>
                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 13,
                  color: "var(--text-muted)",
                }}>
                  streak: {user.streak}
                </span>
                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 14,
                  color: "var(--accent)", fontWeight: 600,
                }}>
                  {user.problems_solved} solved
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
