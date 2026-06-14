"use client";
import Navbar from "@/components/Navbar";
import { FileText, Code2, Cpu, Zap } from "lucide-react";

const sections = [
  {
    icon: <Code2 size={20} color="var(--accent)" />,
    title: "Supported Languages",
    content: [
      { label: "Verilog (.v)", desc: "IEEE 1364 — RTL design for combinational and sequential circuits" },
      { label: "SystemVerilog (.sv)", desc: "IEEE 1800 — Advanced design and verification superset of Verilog" },
    ]
  },
  {
    icon: <Cpu size={20} color="#7c6af7" />,
    title: "How Simulation Works",
    content: [
      { label: "Icarus Verilog", desc: "Your code is compiled and simulated using Icarus Verilog (iverilog)" },
      { label: "Testbenches", desc: "Hidden testbenches verify your design against all test cases" },
      { label: "Waveforms", desc: "VCD waveform data is generated and displayed after every submission" },
    ]
  },
  {
    icon: <Zap size={20} color="#f7a76c" />,
    title: "Problem Difficulty",
    content: [
      { label: "Easy", desc: "Basic gates, simple combinational logic, D flip-flops" },
      { label: "Medium", desc: "FSMs, counters, shift registers, multiplexers" },
      { label: "Hard", desc: "ALUs, LFSRs, interfaces, pipelined designs" },
    ]
  },
  {
    icon: <FileText size={20} color="#f76c8a" />,
    title: "Tips for Success",
    content: [
      { label: "Read the truth table", desc: "Every combinational problem has a truth table — use it" },
      { label: "Use non-blocking assignments", desc: "Always use <= inside always @(posedge clk) blocks" },
      { label: "Test edge cases", desc: "Reset behavior, overflow, and boundary conditions matter" },
      { label: "Use AI hints", desc: "Stuck? Use the AI hint system — 3 hints per problem" },
    ]
  },
];

export default function DocsPage() {
  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{ maxWidth: 900, margin: "0 auto", padding: "48px 24px" }}>
        <div style={{ textAlign: "center", marginBottom: 48 }}>
          <FileText size={40} color="var(--accent)" style={{ marginBottom: 16 }} />
          <h1 style={{ fontSize: 32, fontWeight: 700, marginBottom: 8 }}>Documentation</h1>
          <p style={{ color: "var(--text-muted)" }}>
            Everything you need to know about using BitForge
          </p>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
          {sections.map(section => (
            <div key={section.title} style={{
              background: "var(--bg-surface)",
              border: "1px solid var(--border)",
              borderRadius: 16, padding: 28,
            }}>
              <div style={{ display: "flex", alignItems: "center",
                gap: 10, marginBottom: 20 }}>
                {section.icon}
                <h2 style={{ fontSize: 18, fontWeight: 700 }}>{section.title}</h2>
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                {section.content.map(item => (
                  <div key={item.label} style={{
                    background: "var(--bg-elevated)",
                    borderRadius: 8, padding: "12px 16px",
                  }}>
                    <span style={{
                      fontFamily: "var(--font-mono)", fontSize: 13,
                      color: "var(--accent)", fontWeight: 600,
                    }}>{item.label}</span>
                    <p style={{ fontSize: 13, color: "var(--text-muted)",
                      marginTop: 4, lineHeight: 1.6 }}>{item.desc}</p>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
