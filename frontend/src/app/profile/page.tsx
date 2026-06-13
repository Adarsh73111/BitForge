"use client";
import { useState, useEffect } from "react";
import Navbar from "@/components/Navbar";
import { User, Trophy, Zap, Code2, TrendingUp } from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function ProfilePage() {
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/users/testuser`)
      .then(r => r.json())
      .then(data => { setProfile(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const stats = profile ? [
    { icon: <Code2 size={20} color="var(--accent)" />, label: "Problems Solved", value: profile.problems_solved },
    { icon: <TrendingUp size={20} color="#7c6af7" />,  label: "Total Submissions", value: profile.total_submissions },
    { icon: <Trophy size={20} color="#f7a76c" />,      label: "Pass Rate", value: `${profile.pass_rate}%` },
    { icon: <Zap size={20} color="#f76c8a" />,         label: "Day Streak", value: profile.streak },
  ] : [];

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{ maxWidth: 900, margin: "0 auto", padding: "48px 24px" }}>

        {loading ? (
          <div style={{ textAlign: "center", color: "var(--text-muted)", padding: 80 }}>
            Loading profile...
          </div>
        ) : !profile ? (
          <div style={{ textAlign: "center", color: "var(--text-muted)", padding: 80 }}>
            Profile not found
          </div>
        ) : (
          <>
            {/* Profile Header */}
            <div style={{
              display: "flex", alignItems: "center", gap: 24,
              background: "var(--bg-surface)",
              border: "1px solid var(--border)",
              borderRadius: 16, padding: 32, marginBottom: 24,
            }}>
              <div style={{
                width: 80, height: 80, borderRadius: "50%",
                background: "var(--accent-dim)",
                border: "2px solid var(--accent)",
                display: "flex", alignItems: "center", justifyContent: "center",
              }}>
                <User size={36} color="var(--accent)" />
              </div>
              <div>
                <h1 style={{ fontSize: 28, fontWeight: 700, marginBottom: 4 }}>
                  {profile.username}
                </h1>
                <p style={{ color: "var(--text-muted)", fontSize: 14 }}>
                  {profile.email}
                </p>
                <p style={{ color: "var(--text-muted)", fontSize: 12, marginTop: 4,
                  fontFamily: "var(--font-mono)" }}>
                  Member since {new Date(profile.created_at).toLocaleDateString()}
                </p>
              </div>
            </div>

            {/* Stats Grid */}
            <div style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
              gap: 16, marginBottom: 24,
            }}>
              {stats.map(s => (
                <div key={s.label} style={{
                  background: "var(--bg-surface)",
                  border: "1px solid var(--border)",
                  borderRadius: 12, padding: 24,
                  textAlign: "center",
                }}>
                  <div style={{ display: "flex", justifyContent: "center", marginBottom: 12 }}>
                    {s.icon}
                  </div>
                  <div style={{
                    fontFamily: "var(--font-mono)", fontSize: 32,
                    fontWeight: 700, color: "var(--text-primary)", marginBottom: 4,
                  }}>{s.value}</div>
                  <div style={{ fontSize: 12, color: "var(--text-muted)" }}>{s.label}</div>
                </div>
              ))}
            </div>

            {/* Progress by Difficulty */}
            <div style={{
              background: "var(--bg-surface)",
              border: "1px solid var(--border)",
              borderRadius: 16, padding: 28,
            }}>
              <h2 style={{ fontSize: 18, fontWeight: 600, marginBottom: 24 }}>
                Progress
              </h2>
              {[
                { label: "Easy",   color: "#00d4aa", total: 14 },
                { label: "Medium", color: "#f7a76c", total: 12 },
                { label: "Hard",   color: "#ff4d6a", total: 4  },
              ].map(d => (
                <div key={d.label} style={{ marginBottom: 16 }}>
                  <div style={{
                    display: "flex", justifyContent: "space-between",
                    marginBottom: 6,
                  }}>
                    <span style={{ fontSize: 13, color: d.color }}>{d.label}</span>
                    <span style={{
                      fontSize: 12, color: "var(--text-muted)",
                      fontFamily: "var(--font-mono)",
                    }}>
                      {profile.problems_solved > 0 ? Math.min(profile.problems_solved, d.total) : 0}/{d.total}
                    </span>
                  </div>
                  <div style={{
                    height: 6, background: "var(--bg-elevated)",
                    borderRadius: 3, overflow: "hidden",
                  }}>
                    <div style={{
                      height: "100%", borderRadius: 3,
                      background: d.color,
                      width: `${(Math.min(profile.problems_solved, d.total) / d.total) * 100}%`,
                      transition: "width 0.5s ease",
                    }} />
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
