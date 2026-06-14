"use client";
import Navbar from "@/components/Navbar";
import Link from "next/link";
import { BookOpen, ChevronRight } from "lucide-react";

const tracks = [
  {
    title: "RTL Design Fundamentals",
    description: "Master combinational and sequential circuit design from gates to FSMs",
    problems: 14, color: "#00d4aa",
    topics: ["AND/OR/XOR Gates", "Adders", "Multiplexers", "Flip-Flops", "Counters", "FSMs"],
  },
  {
    title: "ASIC Interview Prep",
    description: "Problems commonly asked in Intel, Qualcomm, and AMD interviews",
    problems: 12, color: "#7c6af7",
    topics: ["ALU Design", "Shift Registers", "LFSR", "Pipeline", "Gray Code", "Parity"],
  },
  {
    title: "FPGA for Beginners",
    description: "Start your FPGA journey with practical Verilog design problems",
    problems: 10, color: "#f7a76c",
    topics: ["Basic Gates", "Counters", "PWM", "Debounce", "Ring Counter", "Clock Divider"],
  },
  {
    title: "SystemVerilog Verification",
    description: "Learn verification techniques with assertions and testbenches",
    problems: 8, color: "#f76c8a",
    topics: ["Assertions", "Testbenches", "Coverage", "Constrained Random", "Scoreboards"],
  },
];

export default function TracksPage() {
  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{ maxWidth: 1000, margin: "0 auto", padding: "48px 24px" }}>
        <div style={{ textAlign: "center", marginBottom: 48 }}>
          <BookOpen size={40} color="var(--accent)" style={{ marginBottom: 16 }} />
          <h1 style={{ fontSize: 32, fontWeight: 700, marginBottom: 8 }}>Learning Tracks</h1>
          <p style={{ color: "var(--text-muted)" }}>
            Structured paths to master Verilog and SystemVerilog
          </p>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(450px, 1fr))", gap: 24 }}>
          {tracks.map(track => (
            <div key={track.title} style={{
              background: "var(--bg-surface)",
              border: `1px solid ${track.color}33`,
              borderRadius: 16, padding: 28,
            }}>
              <div style={{ display: "flex", justifyContent: "space-between",
                alignItems: "flex-start", marginBottom: 12 }}>
                <h2 style={{ fontSize: 18, fontWeight: 700 }}>{track.title}</h2>
                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 12,
                  color: track.color, background: `${track.color}22`,
                  padding: "3px 10px", borderRadius: 4,
                }}>{track.problems} problems</span>
              </div>
              <p style={{ color: "var(--text-muted)", fontSize: 14,
                lineHeight: 1.6, marginBottom: 16 }}>{track.description}</p>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 20 }}>
                {track.topics.map(topic => (
                  <span key={topic} style={{
                    fontSize: 11, padding: "3px 8px", borderRadius: 4,
                    background: "var(--bg-elevated)",
                    color: "var(--text-muted)",
                    fontFamily: "var(--font-mono)",
                  }}>{topic}</span>
                ))}
              </div>
              <Link href="/problems" style={{
                display: "flex", alignItems: "center", gap: 6,
                color: track.color, textDecoration: "none",
                fontSize: 14, fontWeight: 600,
              }}>
                Start Track <ChevronRight size={14} />
              </Link>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
