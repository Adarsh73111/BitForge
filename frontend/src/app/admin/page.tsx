"use client";
import { useState, useEffect } from "react";
import Navbar from "@/components/Navbar";
import dynamic from "next/dynamic";
import { Plus, Save, Trash2, TestTube, LogIn } from "lucide-react";

const MonacoEditor = dynamic(() => import("@monaco-editor/react"), { ssr: false });

const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function AdminPage() {
  const [adminKey,  setAdminKey]  = useState("");
  const [authed,    setAuthed]    = useState(false);
  const [problems,  setProblems]  = useState<any[]>([]);
  const [selected,  setSelected]  = useState<any>(null);
  const [msg,       setMsg]       = useState("");
  const [form,      setForm]      = useState({
    title: "", slug: "", difficulty: "easy",
    category: "combinational", description: "",
    starter_code: "", testbench: "",
    hints: "", company_tags: "",
  });

  const headers = {
    "Content-Type": "application/json",
    "x-admin-key": adminKey,
  };

  const login = async () => {
    const res = await fetch(`${API}/admin/problems`, { headers });
    if (res.ok) {
      const data = await res.json();
      setProblems(data);
      setAuthed(true);
    } else {
      setMsg("❌ Invalid admin key");
    }
  };

  const loadProblems = async () => {
    const res = await fetch(`${API}/admin/problems`, { headers });
    if (res.ok) setProblems(await res.json());
  };

  const createProblem = async () => {
    const body = {
      ...form,
      hints:        form.hints.split("\n").filter(Boolean),
      company_tags: form.company_tags.split(",").map(t => t.trim()).filter(Boolean),
    };
    const res = await fetch(`${API}/admin/problems`, {
      method: "POST", headers, body: JSON.stringify(body),
    });
    if (res.ok) {
      setMsg("✅ Problem created!"); loadProblems();
      setForm({ title:"",slug:"",difficulty:"easy",category:"combinational",
        description:"",starter_code:"",testbench:"",hints:"",company_tags:"" });
    } else {
      const err = await res.json();
      setMsg(`❌ ${err.detail}`);
    }
  };

  const deleteProblem = async (id: number) => {
    if (!confirm("Delete this problem?")) return;
    const res = await fetch(`${API}/admin/problems/${id}`, {
      method: "DELETE", headers,
    });
    if (res.ok) { setMsg("✅ Deleted"); loadProblems(); }
  };

  const testProblem = async (id: number) => {
    setMsg("🔄 Testing...");
    const res = await fetch(`${API}/admin/problems/${id}/test`, {
      method: "POST", headers,
    });
    const data = await res.json();
    setMsg(`${data.test_result === "passed" ? "✅" : "❌"} ${data.title}: ${data.test_result} — ${data.output?.slice(0,100)}`);
  };

  if (!authed) return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{
        maxWidth: 400, margin: "100px auto", padding: 24,
        background: "var(--bg-surface)",
        border: "1px solid var(--border)", borderRadius: 16,
      }}>
        <h1 style={{ fontSize: 24, fontWeight: 700, marginBottom: 24,
          textAlign: "center" }}>Admin Panel</h1>
        <input
          type="password"
          placeholder="Enter admin key"
          value={adminKey}
          onChange={e => setAdminKey(e.target.value)}
          onKeyDown={e => e.key === "Enter" && login()}
          style={{
            width: "100%", padding: "10px 14px",
            background: "var(--bg-elevated)",
            border: "1px solid var(--border)",
            color: "var(--text-primary)",
            borderRadius: 8, fontSize: 14,
            fontFamily: "var(--font-mono)",
            marginBottom: 12, boxSizing: "border-box",
          }}
        />
        {msg && <p style={{ color: "#ff4d6a", fontSize: 13, marginBottom: 12 }}>{msg}</p>}
        <button onClick={login} style={{
          width: "100%", background: "var(--accent)",
          color: "#0a0a0f", border: "none", cursor: "pointer",
          fontWeight: 700, fontSize: 15, padding: "10px",
          borderRadius: 8, display: "flex", alignItems: "center",
          justifyContent: "center", gap: 8,
        }}>
          <LogIn size={16} /> Login
        </button>
      </div>
    </div>
  );

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg-base)" }}>
      <Navbar />
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "32px 24px" }}>
        <div style={{ display: "flex", justifyContent: "space-between",
          alignItems: "center", marginBottom: 32 }}>
          <h1 style={{ fontSize: 28, fontWeight: 700 }}>Admin Panel</h1>
          <span style={{ fontFamily: "var(--font-mono)", fontSize: 13,
            color: "var(--accent)" }}>{problems.length} problems</span>
        </div>

        {msg && (
          <div style={{
            background: "var(--bg-surface)", border: "1px solid var(--border)",
            borderRadius: 8, padding: "10px 16px", marginBottom: 16,
            fontSize: 13, color: "var(--text-muted)",
          }}>{msg}</div>
        )}

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1.5fr", gap: 24 }}>

          {/* Problem List */}
          <div>
            <h2 style={{ fontSize: 16, fontWeight: 600, marginBottom: 16 }}>
              All Problems
            </h2>
            <div style={{ display: "flex", flexDirection: "column", gap: 8,
              maxHeight: "70vh", overflowY: "auto" }}>
              {problems.map(p => (
                <div key={p.id} style={{
                  background: "var(--bg-surface)",
                  border: `1px solid ${selected?.id === p.id ? "var(--accent)" : "var(--border)"}`,
                  borderRadius: 8, padding: "12px 16px",
                  display: "flex", alignItems: "center", gap: 8,
                  cursor: "pointer",
                }} onClick={() => setSelected(p)}>
                  <span style={{ flex: 1, fontSize: 13 }}>{p.title}</span>
                  <button onClick={(e) => { e.stopPropagation(); testProblem(p.id); }}
                    style={{ background: "none", border: "none", cursor: "pointer",
                      color: "var(--accent)", padding: 4 }}>
                    <TestTube size={14} />
                  </button>
                  <button onClick={(e) => { e.stopPropagation(); deleteProblem(p.id); }}
                    style={{ background: "none", border: "none", cursor: "pointer",
                      color: "#ff4d6a", padding: 4 }}>
                    <Trash2 size={14} />
                  </button>
                </div>
              ))}
            </div>
          </div>

          {/* Create New Problem Form */}
          <div>
            <h2 style={{ fontSize: 16, fontWeight: 600, marginBottom: 16 }}>
              Create New Problem
            </h2>
            <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              {[
                ["Title", "title", "text"],
                ["Slug (url-friendly)", "slug", "text"],
              ].map(([label, key, type]) => (
                <div key={key}>
                  <label style={{ fontSize: 12, color: "var(--text-muted)",
                    display: "block", marginBottom: 4 }}>{label}</label>
                  <input type={type} value={(form as any)[key]}
                    onChange={e => setForm(f => ({...f, [key]: e.target.value}))}
                    style={{ width: "100%", padding: "8px 12px",
                      background: "var(--bg-elevated)",
                      border: "1px solid var(--border)",
                      color: "var(--text-primary)", borderRadius: 6,
                      fontSize: 13, boxSizing: "border-box" as any }} />
                </div>
              ))}

              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
                {[
                  ["Difficulty", "difficulty", ["easy","medium","hard"]],
                  ["Category", "category", ["combinational","sequential","verification"]],
                ].map(([label, key, opts]) => (
                  <div key={key as string}>
                    <label style={{ fontSize: 12, color: "var(--text-muted)",
                      display: "block", marginBottom: 4 }}>{label as string}</label>
                    <select value={(form as any)[key as string]}
                      onChange={e => setForm(f => ({...f, [key as string]: e.target.value}))}
                      style={{ width: "100%", padding: "8px 12px",
                        background: "var(--bg-elevated)",
                        border: "1px solid var(--border)",
                        color: "var(--text-primary)", borderRadius: 6,
                        fontSize: 13 }}>
                      {(opts as string[]).map(o => <option key={o} value={o}>{o}</option>)}
                    </select>
                  </div>
                ))}
              </div>

              <div>
                <label style={{ fontSize: 12, color: "var(--text-muted)",
                  display: "block", marginBottom: 4 }}>Description (Markdown)</label>
                <textarea value={form.description} rows={4}
                  onChange={e => setForm(f => ({...f, description: e.target.value}))}
                  style={{ width: "100%", padding: "8px 12px",
                    background: "var(--bg-elevated)",
                    border: "1px solid var(--border)",
                    color: "var(--text-primary)", borderRadius: 6,
                    fontSize: 12, fontFamily: "var(--font-mono)",
                    resize: "vertical", boxSizing: "border-box" as any }} />
              </div>

              <div>
                <label style={{ fontSize: 12, color: "var(--text-muted)",
                  display: "block", marginBottom: 4 }}>Starter Code</label>
                <div style={{ height: 150, border: "1px solid var(--border)",
                  borderRadius: 6, overflow: "hidden" }}>
                  <MonacoEditor height="150px" language="verilog" theme="vs-dark"
                    value={form.starter_code}
                    onChange={v => setForm(f => ({...f, starter_code: v||""}))}
                    options={{ fontSize: 12, minimap: { enabled: false },
                      lineNumbers: "on" as const }} />
                </div>
              </div>

              <div>
                <label style={{ fontSize: 12, color: "var(--text-muted)",
                  display: "block", marginBottom: 4 }}>Testbench (hidden from users)</label>
                <div style={{ height: 150, border: "1px solid var(--border)",
                  borderRadius: 6, overflow: "hidden" }}>
                  <MonacoEditor height="150px" language="verilog" theme="vs-dark"
                    value={form.testbench}
                    onChange={v => setForm(f => ({...f, testbench: v||""}))}
                    options={{ fontSize: 12, minimap: { enabled: false },
                      lineNumbers: "on" as const }} />
                </div>
              </div>

              <div>
                <label style={{ fontSize: 12, color: "var(--text-muted)",
                  display: "block", marginBottom: 4 }}>Hints (one per line)</label>
                <textarea value={form.hints} rows={3}
                  onChange={e => setForm(f => ({...f, hints: e.target.value}))}
                  placeholder="Use the & operator&#10;assign y = a & b;"
                  style={{ width: "100%", padding: "8px 12px",
                    background: "var(--bg-elevated)",
                    border: "1px solid var(--border)",
                    color: "var(--text-primary)", borderRadius: 6,
                    fontSize: 12, fontFamily: "var(--font-mono)",
                    resize: "vertical", boxSizing: "border-box" as any }} />
              </div>

              <div>
                <label style={{ fontSize: 12, color: "var(--text-muted)",
                  display: "block", marginBottom: 4 }}>Company Tags (comma separated)</label>
                <input type="text" value={form.company_tags}
                  onChange={e => setForm(f => ({...f, company_tags: e.target.value}))}
                  placeholder="Intel, Qualcomm, AMD"
                  style={{ width: "100%", padding: "8px 12px",
                    background: "var(--bg-elevated)",
                    border: "1px solid var(--border)",
                    color: "var(--text-primary)", borderRadius: 6,
                    fontSize: 13, boxSizing: "border-box" as any }} />
              </div>

              <button onClick={createProblem} style={{
                background: "var(--accent)", color: "#0a0a0f",
                border: "none", cursor: "pointer",
                fontWeight: 700, fontSize: 14, padding: "12px",
                borderRadius: 8, display: "flex",
                alignItems: "center", justifyContent: "center", gap: 8,
              }}>
                <Plus size={16} /> Create Problem
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
