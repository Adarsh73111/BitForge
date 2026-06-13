"use client";
import { useState, useEffect } from "react";
import { useParams } from "next/navigation";
import dynamic from "next/dynamic";
import Navbar from "@/components/Navbar";
import WaveformViewer from "@/components/WaveformViewer";
import { Play, Loader2, CheckCircle, XCircle, AlertCircle } from "lucide-react";

const MonacoEditor = dynamic(() => import("@monaco-editor/react"), { ssr: false });

const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function ProblemPage() {
  const { slug } = useParams();
  const [problem,  setProblem]  = useState<any>(null);
  const [code,     setCode]     = useState("");
  const [language, setLanguage] = useState("verilog");
  const [result,   setResult]   = useState<any>(null);
  const [loading,  setLoading]  = useState(false);
  const [fetching, setFetching] = useState(true);

  useEffect(() => {
    fetch(`${API}/problems/${slug}`)
      .then(r => r.json())
      .then(data => {
        setProblem(data);
        setCode(data.starter_code || "");
        setFetching(false);
      })
      .catch(() => setFetching(false));
  }, [slug]);

  const handleSubmit = async () => {
    if (!problem || !code) return;
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch(`${API}/submissions/`, {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          problem_id: problem.id,
          code,
          language,
        }),
      });
      const data = await res.json();
      setResult(data);
    } catch (e) {
      setResult({ status: "error", output: "Connection error" });
    } finally {
      setLoading(false);
    }
  };

  const statusIcon = {
    passed: <CheckCircle size={16} color="#00d4aa" />,
    failed: <XCircle    size={16} color="#ff4d6a" />,
    error:  <AlertCircle size={16} color="#f7a76c" />,
  };

  const statusColor = {
    passed: "#00d4aa",
    failed: "#ff4d6a",
    error:  "#f7a76c",
  };

  if (fetching) return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{ display: "flex", justifyContent: "center", padding: 80 }}>
        <Loader2 size={32} color="var(--accent)" className="animate-spin" />
      </div>
    </div>
  );

  if (!problem) return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{ textAlign: "center", padding: 80, color: "var(--text-muted)" }}>
        Problem not found
      </div>
    </div>
  );

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />

      <div style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        height: "calc(100vh - 60px)",
        gap: 0,
      }}>

        {/* Left — Problem Description */}
        <div style={{
          borderRight: "1px solid var(--border)",
          overflowY: "auto",
          padding: 32,
        }}>
          {/* Header */}
          <div style={{ marginBottom: 24 }}>
            <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
              <span style={{
                fontFamily: "var(--font-mono)", fontSize: 11,
                padding: "3px 10px", borderRadius: 4,
                background: problem.difficulty === "easy"   ? "#00d4aa22" :
                            problem.difficulty === "medium" ? "#f7a76c22" : "#ff4d6a22",
                color:      problem.difficulty === "easy"   ? "#00d4aa"   :
                            problem.difficulty === "medium" ? "#f7a76c"   : "#ff4d6a",
              }}>{problem.difficulty}</span>
              <span style={{
                fontFamily: "var(--font-mono)", fontSize: 11,
                padding: "3px 10px", borderRadius: 4,
                background: "var(--bg-elevated)",
                color: "var(--text-muted)",
              }}>{problem.category}</span>
            </div>
            <h1 style={{ fontSize: 22, fontWeight: 700, marginBottom: 8 }}>
              {problem.title}
            </h1>
            {problem.company_tags?.length > 0 && (
              <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
                {problem.company_tags.map((tag: string) => (
                  <span key={tag} style={{
                    fontSize: 11, padding: "2px 8px",
                    borderRadius: 4,
                    border: "1px solid var(--border)",
                    color: "var(--text-muted)",
                    fontFamily: "var(--font-mono)",
                  }}>{tag}</span>
                ))}
              </div>
            )}
          </div>

          {/* Description */}
          <div style={{
            color: "var(--text-muted)", fontSize: 14,
            lineHeight: 1.8, whiteSpace: "pre-wrap",
          }}>
            {problem.description}
          </div>

          {/* Hints */}
          {problem.hints?.length > 0 && (
            <div style={{ marginTop: 24 }}>
              <p style={{
                fontFamily: "var(--font-mono)", fontSize: 12,
                color: "var(--accent)", marginBottom: 8,
                textTransform: "uppercase", letterSpacing: 1,
              }}>Hints</p>
              {problem.hints.map((hint: string, i: number) => (
                <div key={i} style={{
                  background: "var(--bg-elevated)",
                  border: "1px solid var(--border)",
                  borderRadius: 8, padding: "10px 14px",
                  marginBottom: 8, fontSize: 13,
                  color: "var(--text-muted)",
                }}>
                  {hint}
                </div>
              ))}
            </div>
          )}

          {/* Result Panel */}
          {result && (
            <div style={{
              marginTop: 24,
              background: "var(--bg-surface)",
              border: `1px solid ${(statusColor as any)[result.status] || "var(--border)"}44`,
              borderRadius: 12, padding: 20,
            }}>
              <div style={{
                display: "flex", alignItems: "center",
                gap: 8, marginBottom: 12,
              }}>
                {(statusIcon as any)[result.status]}
                <span style={{
                  fontWeight: 600, fontSize: 14,
                  color: (statusColor as any)[result.status],
                }}>
                  {result.status === "passed" ? "All tests passed!" :
                   result.status === "failed" ? "Tests failed" : "Error"}
                </span>
                {result.runtime_ms && (
                  <span style={{
                    marginLeft: "auto",
                    fontFamily: "var(--font-mono)",
                    fontSize: 12, color: "var(--text-muted)",
                  }}>{result.runtime_ms}ms</span>
                )}
              </div>

              {result.output && (
                <pre style={{
                  fontFamily: "var(--font-mono)", fontSize: 12,
                  color: "var(--text-muted)", whiteSpace: "pre-wrap",
                  background: "var(--bg-base)",
                  padding: 12, borderRadius: 8,
                  maxHeight: 200, overflowY: "auto",
                }}>{result.output}</pre>
              )}

              {/* Waveform Viewer */}
              {result.waveform && (
                <WaveformViewer
                  waveform={result.waveform}
                  status={result.status}
                />
              )}
            </div>
          )}
        </div>

        {/* Right — Code Editor */}
        <div style={{ display: "flex", flexDirection: "column" }}>

          {/* Editor Toolbar */}
          <div style={{
            display: "flex", alignItems: "center",
            justifyContent: "space-between",
            padding: "10px 16px",
            borderBottom: "1px solid var(--border)",
            background: "var(--bg-surface)",
          }}>
            <select
              value={language}
              onChange={e => setLanguage(e.target.value)}
              style={{
                background: "var(--bg-elevated)",
                border: "1px solid var(--border)",
                color: "var(--text-primary)",
                fontFamily: "var(--font-mono)",
                fontSize: 13, padding: "4px 10px",
                borderRadius: 6, cursor: "pointer",
              }}
            >
              <option value="verilog">Verilog (.v)</option>
              <option value="systemverilog">SystemVerilog (.sv)</option>
            </select>

            <button
              onClick={handleSubmit}
              disabled={loading}
              style={{
                background: loading ? "var(--bg-elevated)" : "var(--accent)",
                color: loading ? "var(--text-muted)" : "#0a0a0f",
                border: "none", cursor: loading ? "not-allowed" : "pointer",
                fontWeight: 700, fontSize: 14,
                padding: "8px 20px", borderRadius: 8,
                display: "flex", alignItems: "center", gap: 8,
                transition: "all 0.2s",
              }}
            >
              {loading
                ? <><Loader2 size={14} /> Running...</>
                : <><Play size={14} /> Submit</>
              }
            </button>
          </div>

          {/* Monaco Editor */}
          <div style={{ flex: 1 }}>
            <MonacoEditor
              height="100%"
              language={language === "systemverilog" ? "systemverilog" : "verilog"}
              theme="vs-dark"
              value={code}
              onChange={v => setCode(v || "")}
              options={{
                fontSize:         14,
                fontFamily:       "JetBrains Mono, monospace",
                minimap:          { enabled: false },
                scrollBeyondLastLine: false,
                lineNumbers:      "on",
                automaticLayout:  true,
                tabSize:          2,
                wordWrap:         "on",
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
