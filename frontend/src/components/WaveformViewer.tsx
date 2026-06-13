"use client";
import { useEffect, useRef } from "react";

interface Signal {
  name: string;
  width: number;
  changes: { time: number; value: string }[];
}

interface WaveformData {
  signals: Signal[];
  timescale: string;
  duration: number;
}

interface Props {
  waveform: WaveformData;
  status: "passed" | "failed" | "error";
}

const COLORS = {
  passed: "#00d4aa",
  failed: "#ff4d6a",
  error:  "#f7a76c",
};

const ROW_HEIGHT  = 40;
const LABEL_WIDTH = 120;
const PADDING     = 16;

export default function WaveformViewer({ waveform, status }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const color = COLORS[status] || COLORS.passed;

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || !waveform?.signals?.length) return;

    const ctx    = canvas.getContext("2d");
    if (!ctx) return;

    const signals  = waveform.signals.slice(0, 8); // max 8 signals
    const duration = waveform.duration || 100;
    const width    = canvas.width;
    const waveW    = width - LABEL_WIDTH - PADDING * 2;

    canvas.height  = signals.length * ROW_HEIGHT + PADDING * 2;

    // Background
    ctx.fillStyle = "#0a0a0f";
    ctx.fillRect(0, 0, width, canvas.height);

    // Time grid lines
    const steps = 5;
    for (let i = 0; i <= steps; i++) {
      const x = LABEL_WIDTH + (waveW * i) / steps;
      ctx.strokeStyle = "#2a2a3d";
      ctx.lineWidth   = 1;
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, canvas.height);
      ctx.stroke();

      // Time labels
      const t = Math.round((duration * i) / steps);
      ctx.fillStyle  = "#6b6b8a";
      ctx.font       = "10px JetBrains Mono, monospace";
      ctx.textAlign  = "center";
      ctx.fillText(`${t}`, x, 10);
    }

    signals.forEach((signal, idx) => {
      const y      = PADDING + idx * ROW_HEIGHT;
      const midY   = y + ROW_HEIGHT / 2;
      const highY  = y + 8;
      const lowY   = y + ROW_HEIGHT - 8;

      // Signal label
      ctx.fillStyle = "#e8e8f0";
      ctx.font      = "12px JetBrains Mono, monospace";
      ctx.textAlign = "right";
      ctx.fillText(signal.name, LABEL_WIDTH - 8, midY + 4);

      // Draw waveform
      ctx.strokeStyle = color;
      ctx.lineWidth   = 2;
      ctx.beginPath();

      const changes = signal.changes;
      if (!changes.length) return;

      let prevX  = LABEL_WIDTH;
      let prevVal = changes[0].value;
      let prevY  = prevVal === "1" ? highY : lowY;

      ctx.moveTo(prevX, prevY);

      changes.forEach((change) => {
        const x    = LABEL_WIDTH + (change.time / duration) * waveW;
        const newY = change.value === "1" ? highY : lowY;

        // Horizontal line to transition point
        ctx.lineTo(x, prevY);
        // Vertical transition
        ctx.lineTo(x, newY);

        prevX   = x;
        prevY   = newY;
        prevVal = change.value;
      });

      // Extend to end
      ctx.lineTo(LABEL_WIDTH + waveW, prevY);
      ctx.stroke();

      // Divider
      ctx.strokeStyle = "#2a2a3d";
      ctx.lineWidth   = 1;
      ctx.beginPath();
      ctx.moveTo(0, y + ROW_HEIGHT);
      ctx.lineTo(width, y + ROW_HEIGHT);
      ctx.stroke();
    });

  }, [waveform, status]);

  if (!waveform?.signals?.length) return null;

  return (
    <div style={{
      background:   "var(--bg-surface)",
      border:       `1px solid ${COLORS[status]}44`,
      borderRadius: 12,
      padding:      16,
      marginTop:    16,
    }}>
      <div style={{
        display:        "flex",
        alignItems:     "center",
        gap:            8,
        marginBottom:   12,
      }}>
        <span style={{
          fontFamily: "var(--font-mono)",
          fontSize:   12,
          color:      "var(--text-muted)",
          letterSpacing: 1,
          textTransform: "uppercase",
        }}>
          Waveform — {waveform.timescale}
        </span>
        <span style={{
          fontFamily:  "var(--font-mono)",
          fontSize:    11,
          color:       COLORS[status],
          background:  `${COLORS[status]}22`,
          padding:     "2px 8px",
          borderRadius: 4,
        }}>
          {status.toUpperCase()}
        </span>
      </div>

      <canvas
        ref={canvasRef}
        width={800}
        style={{
          width:        "100%",
          borderRadius: 8,
          display:      "block",
        }}
      />

      <div style={{
        display:   "flex",
        gap:       16,
        marginTop: 8,
        flexWrap:  "wrap",
      }}>
        {waveform.signals.slice(0, 8).map(sig => (
          <span key={sig.name} style={{
            fontFamily: "var(--font-mono)",
            fontSize:   11,
            color:      "var(--text-muted)",
          }}>
            <span style={{ color: COLORS[status] }}>■</span> {sig.name}
          </span>
        ))}
      </div>
    </div>
  );
}
