"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import Navbar from "@/components/Navbar";
import { ChevronRight, Cpu } from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

const diffColor: Record<string, string> = {
  easy:   "#00d4aa",
  medium: "#f7a76c",
  hard:   "#ff4d6a",
};

export default function ProblemsPage() {
  const [problems,   setProblems]   = useState<any[]>([]);
  const [filter,     setFilter]     = useState("all");
  const [loading,    setLoading]    = useState(true);

  useEffect(() => {
    fetch(`${API}/problems/`)
      .then(r => r.json())
      .then(data => { setProblems(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const filtered = filter === "all"
    ? problems
    : problems.filter(p => p.difficulty === filter || p.category === filter);

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />

      <div style={{ maxWidth: 1000, margin: "0 auto", padding: "48px 24px" }}>
        <h1 style={{
          fontFamily: "var(--font-mono)", fontSize: 28,
          fontWeight: 700, marginBottom: 8,
        }}>Problems</h1>
        <p style={{ color: "var(--text-muted)", marginBottom: 32 }}>
          Practice Verilog and SystemVerilog circuit design
        </p>

        {/* Filters */}
        <div style={{ display: "flex", gap: 8, marginBottom: 32, flexWrap: "wrap" }}>
          {["all", "easy", "medium", "hard", "combinational", "sequential", "verification"].map(f => (
            <button key={f} onClick={() => setFilter(f)} style={{
              background: filter === f ? "var(--accent-dim)" : "var(--bg-surface)",
              border: `1px solid ${filter === f ? "var(--accent)" : "var(--border)"}`,
              color: filter === f ? "var(--accent)" : "var(--text-muted)",
              fontFamily: "var(--font-mono)", fontSize: 12,
              padding: "6px 14px", borderRadius: 6,
              cursor: "pointer", textTransform: "capitalize",
            }}>{f}</button>
          ))}
        </div>

        {/* Problem List */}
        {loading ? (
          <div style={{ textAlign: "center", color: "var(--text-muted)", padding: 48 }}>
            Loading problems...
          </div>
        ) : filtered.length === 0 ? (
          <div style={{ textAlign: "center", color: "var(--text-muted)", padding: 48 }}>
            No problems found
          </div>
        ) : (
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            {filtered.map((p, i) => (
              <Link key={p.id} href={`/problems/${p.slug}`} style={{
                textDecoration: "none",
                display: "flex", alignItems: "center",
                background: "var(--bg-surface)",
                border: "1px solid var(--border)",
                borderRadius: 10, padding: "16px 20px",
                transition: "border-color 0.2s",
              }}
                onMouseEnter={e => (e.currentTarget.style.borderColor = "rgba(0,212,170,0.3)")}
                onMouseLeave={e => (e.currentTarget.style.borderColor = "var(--border)")}
              >
                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 13,
                  color: "var(--text-muted)", width: 40,
                }}>{i + 1}.</span>

                <div style={{ flex: 1 }}>
                  <span style={{ fontSize: 15, fontWeight: 500, color: "var(--text-primary)" }}>
                    {p.title}
                  </span>
                  <div style={{ display: "flex", gap: 8, marginTop: 4 }}>
                    <span style={{
                      fontFamily: "var(--font-mono)", fontSize: 11,
                      color: "var(--text-muted)",
                    }}>{p.category}</span>
                    {p.company_tags?.map((tag: string) => (
                      <span key={tag} style={{
                        fontFamily: "var(--font-mono)", fontSize: 11,
                        color: "var(--text-muted)",
                        border: "1px solid var(--border)",
                        padding: "0 6px", borderRadius: 3,
                      }}>{tag}</span>
                    ))}
                  </div>
                </div>

                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 12,
                  color: diffColor[p.difficulty] || "var(--text-muted)",
                  textTransform: "capitalize", marginRight: 16,
                }}>{p.difficulty}</span>

                <ChevronRight size={16} color="var(--text-muted)" />
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
