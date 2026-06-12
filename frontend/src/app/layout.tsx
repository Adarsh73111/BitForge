import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "BitForge — Hardware Coding Platform",
  description: "Write, simulate and verify Verilog & SystemVerilog circuits in your browser. The coding platform for hardware engineers.",
  keywords: ["Verilog", "SystemVerilog", "FPGA", "ASIC", "RTL", "hardware engineering"],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>{children}</body>
    </html>
  );
}
