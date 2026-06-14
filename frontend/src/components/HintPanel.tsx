"use client";
import { useState } from "react";
import { Lightbulb, Loader2, ChevronRight } from "lucide-react";

interface Props {
  problemId:   number;
  userCode:    string;
  errorOutput: string;
  apiUrl:      string;
}

export default function HintPanel({ problemId, userCode, errorOutput, apiUrl }: Props) {
  const [hints,      setHints]      = useState<string[]>([]);
  const [loading,    setLoading]    = useState(false);
  const [hintNumber, setHintNumber] = useState(1);
  const [expanded,   setExpanded]   = useState(false);

  const getHint = async () => {
    if (hintNumber > 3) return;
    setLoading(true);
    try {
      const res = await fetch(`${apiUrl}/hints/`, {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          problem_id:   problemId,
          user_code:    userCode,
          error_output: errorOutput,
          hint_number:  hintNumber,
        }),
      });
      const data = await res.json();
      setHints(prev => [...prev, data.hint]);
      setHintNumber(prev => prev + 1);
      setExpanded(true);
    } catch {
      setHints(prev => [...prev, "Could not load hint. Please try again."]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: 16 }}>
      <div style={{
        display: "flex", alignItems: "center",
        justifyContent: "space-between", cursor: "pointer",
        padding: "10px 0",
      }} onClick={() => setExpanded(!expanded)}>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <Lightbulb size={16} color="#f7a76c" />
          <span style={{ fontSize: 13, fontWeight: 600, color: "#f7a76c" }}>
            AI Hints ({hints.length}/3 used)
          </span>
        </div>
        <ChevronRight size={14} color="var(--text-muted)"
          style={{ transform: expanded ? "rotate(90deg)" : "none",
            transition: "transform 0.2s" }} />
      </div>

      {expanded && (
        <div style={{
          background: "var(--bg-elevated)",
          border: "1px solid rgba(247,167,108,0.2)",
          borderRadius: 10, padding: 16,
        }}>
          {hints.map((hint, i) => (
            <div key={i} style={{ marginBottom: 12 }}>
              <div style={{ marginBottom: 6 }}>
                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 11,
                  color: "#f7a76c",
                  background: "rgba(247,167,108,0.15)",
                  padding: "2px 8px", borderRadius: 4,
                }}>Hint {i + 1}</span>
              </div>
              <p style={{ fontSize: 13, color: "var(--text-muted)",
                lineHeight: 1.7, margin: 0 }}>{hint}</p>
              {i < hints.length - 1 && (
                <hr style={{ border: "none",
                  borderTop: "1px solid var(--border)", margin: "12px 0" }} />
              )}
            </div>
          ))}

          {hintNumber <= 3 ? (
            <button onClick={getHint} disabled={loading} style={{
              background: loading ? "var(--bg-base)" : "rgba(247,167,108,0.15)",
              border: "1px solid rgba(247,167,108,0.3)",
              color: "#f7a76c", cursor: loading ? "not-allowed" : "pointer",
              fontSize: 13, fontWeight: 600,
              padding: "8px 16px", borderRadius: 6,
              display: "flex", alignItems: "center", gap: 6,
              marginTop: hints.length > 0 ? 12 : 0,
              width: "100%", justifyContent: "center",
            }}>
              {loading
                ? <><Loader2 size={13} /> Getting hint...</>
                : <><Lightbulb size={13} />
                    {hints.length === 0 ? "Get a hint" : `Get hint ${hintNumber}/3`}
                  </>
              }
            </button>
          ) : (
            <p style={{ fontSize: 12, color: "var(--text-muted)",
              textAlign: "center", marginTop: 8 }}>
              All 3 hints used — try submitting your solution! 💪
            </p>
          )}
        </div>
      )}
    </div>
  );
}
