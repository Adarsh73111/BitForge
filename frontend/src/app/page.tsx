"use client";
import Navbar from "@/components/Navbar";
import Link from "next/link";
import { Zap, Cpu, GitBranch, Award, ChevronRight, Code2, Layers, Shield } from "lucide-react";

const stats = [
  { value: "30+", label: "Problems" },
  { value: "2", label: "Languages" },
  { value: "Live", label: "Waveforms" },
  { value: "Free", label: "Forever" },
];

const features = [
  {
    icon: <Code2 size={22} color="var(--accent)" />,
    title: "Verilog & SystemVerilog",
    desc: "Write synthesizable RTL for combinational and sequential circuits. Full syntax highlighting via Monaco Editor."
  },
  {
    icon: <Layers size={22} color="var(--accent)" />,
    title: "Live Waveform Viewer",
    desc: "See your circuit signals animate in real time after every simulation. Debug visually, not blindly."
  },
  {
    icon: <Shield size={22} color="var(--accent)" />,
    title: "Verification Challenges",
    desc: "Write SystemVerilog testbenches and assertions to catch bugs. Just like real ASIC/FPGA verification work."
  },
  {
    icon: <Award size={22} color="var(--accent)" />,
    title: "Company-Tagged Problems",
    desc: "Practice with problems tagged by Intel, Qualcomm, AMD and more. Built for hardware job seekers."
  },
  {
    icon: <GitBranch size={22} color="var(--accent)" />,
    title: "Learning Tracks",
    desc: "Structured paths from basic gates to full UART/SPI interfaces. Follow a curriculum or jump in anywhere."
  },
  {
    icon: <Cpu size={22} color="var(--accent)" />,
    title: "Instant Simulation",
    desc: "Icarus Verilog runs your code in a secure sandbox. Compile, simulate and get results in seconds."
  },
];

const categories = [
  { name: "Combinational Logic", count: 10, color: "#00d4aa" },
  { name: "Sequential Circuits", count: 10, color: "#7c6af7" },
  { name: "Finite State Machines", count: 6, color: "#f7a76c" },
  { name: "Pipelined Design", count: 5, color: "#f76c8a" },
  { name: "SV Verification", count: 8, color: "#6cf7d4" },
  { name: "Interfaces (UART/SPI)", count: 5, color: "#f7e26c" },
];

export default function Home() {
  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />

      {/* Hero */}
      <section style={{
        maxWidth: 1200, margin: "0 auto", padding: "100px 24px 80px",
        textAlign: "center", position: "relative",
      }}>
        <div style={{
          position: "absolute", inset: 0, opacity: 0.03,
          backgroundImage: `
            linear-gradient(var(--accent) 1px, transparent 1px),
            linear-gradient(90deg, var(--accent) 1px, transparent 1px)
          `,
          backgroundSize: "40px 40px",
          pointerEvents: "none",
        }} />

        <div style={{
          display: "inline-flex", alignItems: "center", gap: 8,
          background: "var(--accent-dim)", border: "1px solid rgba(0,212,170,0.3)",
          borderRadius: 100, padding: "6px 16px", marginBottom: 32,
        }}>
          <Zap size={12} color="var(--accent)" />
          <span style={{ color: "var(--accent)", fontSize: 13, fontFamily: "var(--font-mono)" }}>
            Now in development — Verilog + SystemVerilog
          </span>
        </div>

        <h1 style={{
          fontSize: "clamp(36px, 6vw, 72px)",
          fontWeight: 700, lineHeight: 1.1,
          marginBottom: 24,
          fontFamily: "var(--font-mono)",
        }}>
          Code hardware.<br />
          <span style={{ color: "var(--accent)" }}>Simulate instantly.</span>
        </h1>

        <p style={{
          fontSize: 18, color: "var(--text-muted)", maxWidth: 580,
          margin: "0 auto 48px", lineHeight: 1.7,
        }}>
          BitForge is the coding platform for hardware engineers.
          Write Verilog and SystemVerilog, run real simulations,
          and see your circuit waveforms live — right in the browser.
        </p>

        <div style={{ display: "flex", gap: 16, justifyContent: "center", flexWrap: "wrap" }}>
          <Link href="/problems" style={{
            background: "var(--accent)", color: "#0a0a0f",
            textDecoration: "none", fontWeight: 700, fontSize: 15,
            padding: "12px 28px", borderRadius: 8,
            display: "flex", alignItems: "center", gap: 8,
          }}>
            Start Solving <ChevronRight size={16} />
          </Link>
          <Link href="/tracks" style={{
            background: "var(--bg-elevated)",
            border: "1px solid var(--border)",
            color: "var(--text-primary)",
            textDecoration: "none", fontWeight: 600, fontSize: 15,
            padding: "12px 28px", borderRadius: 8,
          }}>
            View Tracks
          </Link>
        </div>

        <div style={{
          display: "flex", gap: 48, justifyContent: "center",
          marginTop: 72, flexWrap: "wrap",
        }}>
          {stats.map(s => (
            <div key={s.label} style={{ textAlign: "center" }}>
              <div style={{
                fontFamily: "var(--font-mono)", fontSize: 32,
                fontWeight: 700, color: "var(--accent)",
              }}>{s.value}</div>
              <div style={{ fontSize: 13, color: "var(--text-muted)", marginTop: 4 }}>
                {s.label}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Features */}
      <section style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 24px" }}>
        <p style={{
          textAlign: "center", fontFamily: "var(--font-mono)",
          color: "var(--accent)", fontSize: 13, letterSpacing: 2,
          textTransform: "uppercase", marginBottom: 16,
        }}>Platform Features</p>
        <h2 style={{
          textAlign: "center", fontSize: "clamp(24px, 4vw, 40px)",
          fontWeight: 700, marginBottom: 64,
        }}>Built for how hardware engineers actually work</h2>

        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
          gap: 24,
        }}>
          {features.map(f => (
            <div key={f.title} style={{
              background: "var(--bg-surface)",
              border: "1px solid var(--border)",
              borderRadius: 12, padding: 28,
              transition: "border-color 0.2s, transform 0.2s",
            }}
              onMouseEnter={e => {
                (e.currentTarget as HTMLElement).style.borderColor = "rgba(0,212,170,0.4)";
                (e.currentTarget as HTMLElement).style.transform = "translateY(-2px)";
              }}
              onMouseLeave={e => {
                (e.currentTarget as HTMLElement).style.borderColor = "var(--border)";
                (e.currentTarget as HTMLElement).style.transform = "translateY(0)";
              }}
            >
              <div style={{
                width: 44, height: 44, borderRadius: 10,
                background: "var(--accent-dim)",
                display: "flex", alignItems: "center", justifyContent: "center",
                marginBottom: 16,
              }}>{f.icon}</div>
              <h3 style={{ fontWeight: 600, fontSize: 16, marginBottom: 8 }}>{f.title}</h3>
              <p style={{ color: "var(--text-muted)", fontSize: 14, lineHeight: 1.6 }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Problem Categories */}
      <section style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 24px" }}>
        <p style={{
          textAlign: "center", fontFamily: "var(--font-mono)",
          color: "var(--accent)", fontSize: 13, letterSpacing: 2,
          textTransform: "uppercase", marginBottom: 16,
        }}>Problem Categories</p>
        <h2 style={{
          textAlign: "center", fontSize: "clamp(24px, 4vw, 40px)",
          fontWeight: 700, marginBottom: 64,
        }}>Every area of RTL design covered</h2>

        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
          gap: 16,
        }}>
          {categories.map(c => (
            <Link key={c.name} href="/problems" style={{
              background: "var(--bg-surface)",
              border: "1px solid var(--border)",
              borderRadius: 10, padding: "20px 24px",
              textDecoration: "none",
              display: "flex", justifyContent: "space-between", alignItems: "center",
              transition: "border-color 0.2s",
            }}
              onMouseEnter={e => (e.currentTarget.style.borderColor = c.color + "66")}
              onMouseLeave={e => (e.currentTarget.style.borderColor = "var(--border)")}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div style={{
                  width: 8, height: 8, borderRadius: "50%",
                  background: c.color, flexShrink: 0,
                }} />
                <span style={{ color: "var(--text-primary)", fontSize: 14, fontWeight: 500 }}>
                  {c.name}
                </span>
              </div>
              <span style={{
                fontFamily: "var(--font-mono)", fontSize: 13,
                color: "var(--text-muted)",
              }}>{c.count}</span>
            </Link>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 24px" }}>
        <div style={{
          background: "var(--bg-surface)",
          border: "1px solid rgba(0,212,170,0.2)",
          borderRadius: 16, padding: "64px 48px",
          textAlign: "center",
          backgroundImage: `radial-gradient(ellipse at 50% 0%, rgba(0,212,170,0.08) 0%, transparent 60%)`,
        }}>
          <h2 style={{
            fontSize: "clamp(24px, 4vw, 40px)", fontWeight: 700, marginBottom: 16,
          }}>Ready to forge your hardware skills?</h2>
          <p style={{
            color: "var(--text-muted)", fontSize: 16,
            marginBottom: 36, maxWidth: 480, margin: "0 auto 36px",
          }}>
            Join engineers practicing RTL design and verification.
            No install needed — simulate Verilog right in your browser.
          </p>
          <Link href="/signup" style={{
            background: "var(--accent)", color: "#0a0a0f",
            textDecoration: "none", fontWeight: 700, fontSize: 16,
            padding: "14px 36px", borderRadius: 8,
            display: "inline-flex", alignItems: "center", gap: 8,
          }}>
            Get started free <ChevronRight size={18} />
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer style={{
        borderTop: "1px solid var(--border)",
        padding: "32px 24px", textAlign: "center",
      }}>
        <span style={{
          fontFamily: "var(--font-mono)", fontSize: 13,
          color: "var(--text-muted)",
        }}>
          <span style={{ color: "var(--accent)" }}>BitForge</span>
          {" "}— Built for hardware engineers © 2026
        </span>
      </footer>
    </div>
  );
}
