"""
BitForge — Full Problem Bank Seeder
30 problems across Combinational, Sequential, and Verification
"""
from app.core.database import SessionLocal
from app.models.problem import Problem

db = SessionLocal()

# Clear existing problems (fresh seed)
db.query(Problem).delete()
db.commit()
print("🗑️  Cleared existing problems...")

problems = [

# ═══════════════════════════════════════════
# COMBINATIONAL LOGIC — 10 Problems
# ═══════════════════════════════════════════

{
  "title": "AND Gate",
  "slug": "and-gate",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## AND Gate

Design a 2-input AND gate.

**Module Interface:**
```verilog
module and_gate(
    input  wire a,
    input  wire b,
    output wire y
);
```

**Truth Table:**
| a | b | y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
""",
  "starter_code": """module and_gate(
    input  wire a,
    input  wire b,
    output wire y
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_and_gate;
    reg a, b;
    wire y;
    integer failed = 0;
    and_gate uut (.a(a), .b(b), .y(y));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_and_gate);
        a=0;b=0;#10; if(y!==0) begin $display("FAILED: 0&0=%b",y); failed=failed+1; end
        a=0;b=1;#10; if(y!==0) begin $display("FAILED: 0&1=%b",y); failed=failed+1; end
        a=1;b=0;#10; if(y!==0) begin $display("FAILED: 1&0=%b",y); failed=failed+1; end
        a=1;b=1;#10; if(y!==1) begin $display("FAILED: 1&1=%b",y); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use the & operator", "assign y = a & b;"],
  "company_tags": ["Intel", "Qualcomm"],
},

{
  "title": "OR Gate",
  "slug": "or-gate",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## OR Gate

Design a 2-input OR gate.

**Module Interface:**
```verilog
module or_gate(
    input  wire a,
    input  wire b,
    output wire y
);
```

**Truth Table:**
| a | b | y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |
""",
  "starter_code": """module or_gate(
    input  wire a,
    input  wire b,
    output wire y
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_or_gate;
    reg a, b; wire y;
    integer failed = 0;
    or_gate uut (.a(a), .b(b), .y(y));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_or_gate);
        a=0;b=0;#10; if(y!==0) begin $display("FAILED: 0|0=%b",y); failed=failed+1; end
        a=0;b=1;#10; if(y!==1) begin $display("FAILED: 0|1=%b",y); failed=failed+1; end
        a=1;b=0;#10; if(y!==1) begin $display("FAILED: 1|0=%b",y); failed=failed+1; end
        a=1;b=1;#10; if(y!==1) begin $display("FAILED: 1|1=%b",y); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use the | operator", "assign y = a | b;"],
  "company_tags": ["Intel", "AMD"],
},

{
  "title": "XOR Gate",
  "slug": "xor-gate",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## XOR Gate

Design a 2-input XOR (Exclusive OR) gate.

**Module Interface:**
```verilog
module xor_gate(
    input  wire a,
    input  wire b,
    output wire y
);
```

**Truth Table:**
| a | b | y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
""",
  "starter_code": """module xor_gate(
    input  wire a,
    input  wire b,
    output wire y
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_xor_gate;
    reg a, b; wire y;
    integer failed = 0;
    xor_gate uut (.a(a), .b(b), .y(y));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_xor_gate);
        a=0;b=0;#10; if(y!==0) begin $display("FAILED: 0^0=%b",y); failed=failed+1; end
        a=0;b=1;#10; if(y!==1) begin $display("FAILED: 0^1=%b",y); failed=failed+1; end
        a=1;b=0;#10; if(y!==1) begin $display("FAILED: 1^0=%b",y); failed=failed+1; end
        a=1;b=1;#10; if(y!==0) begin $display("FAILED: 1^1=%b",y); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use the ^ operator", "assign y = a ^ b;"],
  "company_tags": ["Qualcomm", "NVIDIA"],
},

{
  "title": "NOT Gate",
  "slug": "not-gate",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## NOT Gate

Design a single-input NOT (inverter) gate.

**Module Interface:**
```verilog
module not_gate(
    input  wire a,
    output wire y
);
```

**Truth Table:**
| a | y |
|---|---|
| 0 | 1 |
| 1 | 0 |
""",
  "starter_code": """module not_gate(
    input  wire a,
    output wire y
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_not_gate;
    reg a; wire y;
    integer failed = 0;
    not_gate uut (.a(a), .y(y));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_not_gate);
        a=0;#10; if(y!==1) begin $display("FAILED: ~0=%b",y); failed=failed+1; end
        a=1;#10; if(y!==0) begin $display("FAILED: ~1=%b",y); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use the ~ operator", "assign y = ~a;"],
  "company_tags": ["Intel", "AMD"],
},

{
  "title": "Half Adder",
  "slug": "half-adder",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## Half Adder

Design a half adder that adds two 1-bit inputs and produces a sum and carry output.

**Module Interface:**
```verilog
module half_adder(
    input  wire a,
    input  wire b,
    output wire sum,
    output wire carry
);
```

**Truth Table:**
| a | b | sum | carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |
""",
  "starter_code": """module half_adder(
    input  wire a,
    input  wire b,
    output wire sum,
    output wire carry
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_half_adder;
    reg a, b; wire sum, carry;
    integer failed = 0;
    half_adder uut (.a(a), .b(b), .sum(sum), .carry(carry));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_half_adder);
        a=0;b=0;#10; if(sum!==0||carry!==0) begin $display("FAILED: 0+0"); failed=failed+1; end
        a=0;b=1;#10; if(sum!==1||carry!==0) begin $display("FAILED: 0+1"); failed=failed+1; end
        a=1;b=0;#10; if(sum!==1||carry!==0) begin $display("FAILED: 1+0"); failed=failed+1; end
        a=1;b=1;#10; if(sum!==0||carry!==1) begin $display("FAILED: 1+1"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["sum = a XOR b", "carry = a AND b", "assign sum = a ^ b; assign carry = a & b;"],
  "company_tags": ["Intel", "Qualcomm", "AMD"],
},

{
  "title": "Full Adder",
  "slug": "full-adder",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## Full Adder

Design a full adder that adds three 1-bit inputs (a, b, cin) and produces sum and carry outputs.

**Module Interface:**
```verilog
module full_adder(
    input  wire a,
    input  wire b,
    input  wire cin,
    output wire sum,
    output wire cout
);
```
""",
  "starter_code": """module full_adder(
    input  wire a,
    input  wire b,
    input  wire cin,
    output wire sum,
    output wire cout
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_full_adder;
    reg a, b, cin; wire sum, cout;
    integer failed = 0;
    full_adder uut (.a(a),.b(b),.cin(cin),.sum(sum),.cout(cout));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_full_adder);
        a=0;b=0;cin=0;#10; if(sum!==0||cout!==0) begin $display("FAILED: 0+0+0"); failed=failed+1; end
        a=0;b=0;cin=1;#10; if(sum!==1||cout!==0) begin $display("FAILED: 0+0+1"); failed=failed+1; end
        a=0;b=1;cin=0;#10; if(sum!==1||cout!==0) begin $display("FAILED: 0+1+0"); failed=failed+1; end
        a=0;b=1;cin=1;#10; if(sum!==0||cout!==1) begin $display("FAILED: 0+1+1"); failed=failed+1; end
        a=1;b=0;cin=0;#10; if(sum!==1||cout!==0) begin $display("FAILED: 1+0+0"); failed=failed+1; end
        a=1;b=0;cin=1;#10; if(sum!==0||cout!==1) begin $display("FAILED: 1+0+1"); failed=failed+1; end
        a=1;b=1;cin=0;#10; if(sum!==0||cout!==1) begin $display("FAILED: 1+1+0"); failed=failed+1; end
        a=1;b=1;cin=1;#10; if(sum!==1||cout!==1) begin $display("FAILED: 1+1+1"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["sum = a ^ b ^ cin", "cout = (a&b) | (b&cin) | (a&cin)"],
  "company_tags": ["Intel", "AMD", "Qualcomm"],
},

{
  "title": "2:1 Multiplexer",
  "slug": "mux-2to1",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## 2:1 Multiplexer

Design a 2-to-1 multiplexer. When sel=0, output y=a. When sel=1, output y=b.

**Module Interface:**
```verilog
module mux2to1(
    input  wire a,
    input  wire b,
    input  wire sel,
    output wire y
);
```
""",
  "starter_code": """module mux2to1(
    input  wire a,
    input  wire b,
    input  wire sel,
    output wire y
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_mux2to1;
    reg a, b, sel; wire y;
    integer failed = 0;
    mux2to1 uut (.a(a),.b(b),.sel(sel),.y(y));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_mux2to1);
        a=0;b=1;sel=0;#10; if(y!==0) begin $display("FAILED: sel=0 y=%b",y); failed=failed+1; end
        a=0;b=1;sel=1;#10; if(y!==1) begin $display("FAILED: sel=1 y=%b",y); failed=failed+1; end
        a=1;b=0;sel=0;#10; if(y!==1) begin $display("FAILED: sel=0 y=%b",y); failed=failed+1; end
        a=1;b=0;sel=1;#10; if(y!==0) begin $display("FAILED: sel=1 y=%b",y); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use ternary operator", "assign y = sel ? b : a;"],
  "company_tags": ["Qualcomm", "NVIDIA"],
},

{
  "title": "4:1 Multiplexer",
  "slug": "mux-4to1",
  "difficulty": "medium",
  "category": "combinational",
  "description": """## 4:1 Multiplexer

Design a 4-to-1 multiplexer with a 2-bit select signal.

**Module Interface:**
```verilog
module mux4to1(
    input  wire d0, d1, d2, d3,
    input  wire [1:0] sel,
    output wire y
);
```

| sel | y  |
|-----|----|
| 00  | d0 |
| 01  | d1 |
| 10  | d2 |
| 11  | d3 |
""",
  "starter_code": """module mux4to1(
    input  wire d0, d1, d2, d3,
    input  wire [1:0] sel,
    output wire y
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_mux4to1;
    reg d0,d1,d2,d3; reg [1:0] sel; wire y;
    integer failed = 0;
    mux4to1 uut (.d0(d0),.d1(d1),.d2(d2),.d3(d3),.sel(sel),.y(y));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_mux4to1);
        d0=1;d1=0;d2=0;d3=0;sel=2'b00;#10; if(y!==1) begin $display("FAILED sel=00"); failed=failed+1; end
        d0=0;d1=1;d2=0;d3=0;sel=2'b01;#10; if(y!==1) begin $display("FAILED sel=01"); failed=failed+1; end
        d0=0;d1=0;d2=1;d3=0;sel=2'b10;#10; if(y!==1) begin $display("FAILED sel=10"); failed=failed+1; end
        d0=0;d1=0;d2=0;d3=1;sel=2'b11;#10; if(y!==1) begin $display("FAILED sel=11"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use case statement or nested ternary", "case(sel) 2'b00: y=d0; ..."],
  "company_tags": ["Intel", "Qualcomm"],
},

{
  "title": "3:8 Decoder",
  "slug": "decoder-3to8",
  "difficulty": "medium",
  "category": "combinational",
  "description": """## 3:8 Decoder

Design a 3-to-8 decoder. Only one output is HIGH at a time based on the 3-bit input.

**Module Interface:**
```verilog
module decoder3to8(
    input  wire [2:0] in,
    output wire [7:0] out
);
```
""",
  "starter_code": """module decoder3to8(
    input  wire [2:0] in,
    output wire [7:0] out
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_decoder3to8;
    reg [2:0] in; wire [7:0] out;
    integer i, failed = 0;
    decoder3to8 uut (.in(in),.out(out));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_decoder3to8);
        for(i=0;i<8;i=i+1) begin
            in=i; #10;
            if(out !== (8'b1 << i)) begin
                $display("FAILED: in=%0d out=%b", i, out);
                failed=failed+1;
            end
        end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use assign out = 1 << in;", "Only one bit HIGH at a time"],
  "company_tags": ["AMD", "Intel"],
},

{
  "title": "8-bit Comparator",
  "slug": "comparator-8bit",
  "difficulty": "medium",
  "category": "combinational",
  "description": """## 8-bit Comparator

Design an 8-bit magnitude comparator with three outputs.

**Module Interface:**
```verilog
module comparator_8bit(
    input  wire [7:0] a,
    input  wire [7:0] b,
    output wire eq,   // a == b
    output wire gt,   // a > b
    output wire lt    // a < b
);
```
""",
  "starter_code": """module comparator_8bit(
    input  wire [7:0] a,
    input  wire [7:0] b,
    output wire eq,
    output wire gt,
    output wire lt
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_comparator_8bit;
    reg [7:0] a, b; wire eq, gt, lt;
    integer failed = 0;
    comparator_8bit uut (.a(a),.b(b),.eq(eq),.gt(gt),.lt(lt));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_comparator_8bit);
        a=8'd50; b=8'd50;#10; if(eq!==1||gt!==0||lt!==0) begin $display("FAILED: eq"); failed=failed+1; end
        a=8'd100;b=8'd50; #10; if(eq!==0||gt!==1||lt!==0) begin $display("FAILED: gt"); failed=failed+1; end
        a=8'd10; b=8'd50;#10; if(eq!==0||gt!==0||lt!==1) begin $display("FAILED: lt"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["assign eq = (a == b);", "assign gt = (a > b);", "assign lt = (a < b);"],
  "company_tags": ["Qualcomm", "NVIDIA", "AMD"],
},

# ═══════════════════════════════════════════
# SEQUENTIAL LOGIC — 10 Problems
# ═══════════════════════════════════════════

{
  "title": "D Flip-Flop",
  "slug": "d-flip-flop",
  "difficulty": "easy",
  "category": "sequential",
  "description": """## D Flip-Flop

Design a positive edge-triggered D flip-flop with synchronous reset.

**Module Interface:**
```verilog
module d_flip_flop(
    input  wire clk,
    input  wire rst,
    input  wire d,
    output reg  q
);
```

- On rising edge of clk: if rst=1, q=0; else q=d
""",
  "starter_code": """module d_flip_flop(
    input  wire clk,
    input  wire rst,
    input  wire d,
    output reg  q
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_d_flip_flop;
    reg clk, rst, d; wire q;
    integer failed = 0;
    d_flip_flop uut (.clk(clk),.rst(rst),.d(d),.q(q));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_d_flip_flop);
        rst=1;d=0;#12; if(q!==0) begin $display("FAILED: reset"); failed=failed+1; end
        rst=0;d=1;#10; if(q!==1) begin $display("FAILED: d=1"); failed=failed+1; end
        d=0;#10; if(q!==0) begin $display("FAILED: d=0"); failed=failed+1; end
        d=1;#10; if(q!==1) begin $display("FAILED: d=1 again"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use always @(posedge clk)", "Check rst first inside always block"],
  "company_tags": ["Intel", "Qualcomm", "AMD"],
},

{
  "title": "4-bit Counter",
  "slug": "counter-4bit",
  "difficulty": "easy",
  "category": "sequential",
  "description": """## 4-bit Synchronous Counter

Design a 4-bit synchronous up-counter with synchronous reset.

**Module Interface:**
```verilog
module counter_4bit(
    input  wire       clk,
    input  wire       rst,
    output reg  [3:0] count
);
```

- Counts 0 → 1 → 2 → ... → 15 → 0
- On rst=1: count resets to 0
""",
  "starter_code": """module counter_4bit(
    input  wire       clk,
    input  wire       rst,
    output reg  [3:0] count
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_counter_4bit;
    reg clk, rst; wire [3:0] count;
    integer failed = 0;
    counter_4bit uut (.clk(clk),.rst(rst),.count(count));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_counter_4bit);
        rst=1;#12; rst=0;
        #10; if(count!==1) begin $display("FAILED: count=%0d expected 1",count); failed=failed+1; end
        #10; if(count!==2) begin $display("FAILED: count=%0d expected 2",count); failed=failed+1; end
        #10; if(count!==3) begin $display("FAILED: count=%0d expected 3",count); failed=failed+1; end
        #50; 
        rst=1;#12;
        if(count!==0) begin $display("FAILED: reset count=%0d",count); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use always @(posedge clk)", "count <= count + 1;"],
  "company_tags": ["Intel", "AMD"],
},

{
  "title": "4-bit Shift Register",
  "slug": "shift-register-4bit",
  "difficulty": "easy",
  "category": "sequential",
  "description": """## 4-bit Shift Register (SISO)

Design a 4-bit Serial-In Serial-Out (SISO) shift register.

**Module Interface:**
```verilog
module shift_register(
    input  wire clk,
    input  wire rst,
    input  wire sin,
    output wire sout
);
```

- On each rising clock edge, data shifts left
- sin enters at LSB, sout exits from MSB
""",
  "starter_code": """module shift_register(
    input  wire clk,
    input  wire rst,
    input  wire sin,
    output wire sout
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_shift_register;
    reg clk, rst, sin; wire sout;
    integer failed = 0;
    shift_register uut (.clk(clk),.rst(rst),.sin(sin),.sout(sout));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_shift_register);
        rst=1;#12;rst=0;
        sin=1;#10;
        sin=0;#10;
        sin=1;#10;
        sin=1;#10;
        if(sout!==1) begin $display("FAILED: sout=%b expected 1",sout); failed=failed+1; end
        #10; if(sout!==0) begin $display("FAILED: sout=%b expected 0",sout); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use a 4-bit reg", "Shift: reg <= {reg[2:0], sin};", "sout = reg[3];"],
  "company_tags": ["Qualcomm", "NVIDIA"],
},

{
  "title": "Moore FSM — Sequence Detector",
  "slug": "fsm-sequence-detector",
  "difficulty": "medium",
  "category": "sequential",
  "description": """## Moore FSM — Sequence Detector

Design a Moore FSM that detects the sequence **1011** in a serial input stream.

**Module Interface:**
```verilog
module seq_detector(
    input  wire clk,
    input  wire rst,
    input  wire in,
    output wire detected
);
```

- Output `detected=1` one clock after the complete sequence 1011 is received
- Non-overlapping detection
""",
  "starter_code": """module seq_detector(
    input  wire clk,
    input  wire rst,
    input  wire in,
    output wire detected
);
    // Define states
    // Write your FSM here

endmodule""",
  "testbench": """module tb_seq_detector;
    reg clk, rst, in; wire detected;
    integer failed = 0;
    seq_detector uut (.clk(clk),.rst(rst),.in(in),.detected(detected));
    initial clk = 0;
    always #5 clk = ~clk;
    task send_bit(input b);
        in = b; #10;
    endtask
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_seq_detector);
        rst=1;#12;rst=0;
        send_bit(1);send_bit(0);send_bit(1);send_bit(1);
        #5;
        if(detected!==1) begin $display("FAILED: sequence 1011 not detected"); failed=failed+1; end
        #5;
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Define 5 states: S0(idle), S1(got 1), S2(got 10), S3(got 101), S4(got 1011)",
            "Use parameter for states", "Output detected=1 only in S4"],
  "company_tags": ["Intel", "Qualcomm", "AMD"],
},

{
  "title": "Traffic Light Controller",
  "slug": "traffic-light-fsm",
  "difficulty": "medium",
  "category": "sequential",
  "description": """## Traffic Light Controller (Mealy FSM)

Design a simple traffic light controller FSM.

**Module Interface:**
```verilog
module traffic_light(
    input  wire       clk,
    input  wire       rst,
    output reg  [1:0] light
);
```

**States:**
- light = 2'b00 → RED    (stay 3 cycles)
- light = 2'b01 → GREEN  (stay 3 cycles)
- light = 2'b10 → YELLOW (stay 1 cycle)
- Sequence: RED → GREEN → YELLOW → RED
""",
  "starter_code": """module traffic_light(
    input  wire       clk,
    input  wire       rst,
    output reg  [1:0] light
);
    // Write your FSM here

endmodule""",
  "testbench": """module tb_traffic_light;
    reg clk, rst; wire [1:0] light;
    integer failed = 0;
    traffic_light uut (.clk(clk),.rst(rst),.light(light));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_traffic_light);
        rst=1;#12;rst=0;
        if(light!==2'b00) begin $display("FAILED: should start RED"); failed=failed+1; end
        #30;
        if(light!==2'b01) begin $display("FAILED: should be GREEN"); failed=failed+1; end
        #30;
        if(light!==2'b10) begin $display("FAILED: should be YELLOW"); failed=failed+1; end
        #10;
        if(light!==2'b00) begin $display("FAILED: should return RED"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use a counter to track cycles per state",
            "Use parameter RED=0, GREEN=1, YELLOW=2"],
  "company_tags": ["Intel", "Qualcomm"],
},

{
  "title": "8-bit PIPO Shift Register",
  "slug": "pipo-shift-register",
  "difficulty": "medium",
  "category": "sequential",
  "description": """## 8-bit Parallel-In Parallel-Out Register

Design an 8-bit PIPO register with load and synchronous reset.

**Module Interface:**
```verilog
module pipo_register(
    input  wire       clk,
    input  wire       rst,
    input  wire       load,
    input  wire [7:0] d,
    output reg  [7:0] q
);
```

- When load=1: q <= d on rising edge
- When rst=1: q <= 0
""",
  "starter_code": """module pipo_register(
    input  wire       clk,
    input  wire       rst,
    input  wire       load,
    input  wire [7:0] d,
    output reg  [7:0] q
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_pipo_register;
    reg clk, rst, load; reg [7:0] d; wire [7:0] q;
    integer failed = 0;
    pipo_register uut (.clk(clk),.rst(rst),.load(load),.d(d),.q(q));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_pipo_register);
        rst=1;#12;rst=0;
        if(q!==0) begin $display("FAILED: reset"); failed=failed+1; end
        d=8'hAB;load=1;#10;
        if(q!==8'hAB) begin $display("FAILED: load q=%h",q); failed=failed+1; end
        d=8'hFF;load=0;#10;
        if(q!==8'hAB) begin $display("FAILED: hold q=%h",q); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Check rst first, then load", "Use non-blocking assignment <="],
  "company_tags": ["AMD", "NVIDIA"],
},

{
  "title": "Modulo-6 Counter",
  "slug": "counter-mod6",
  "difficulty": "medium",
  "category": "sequential",
  "description": """## Modulo-6 Counter

Design a synchronous modulo-6 counter that counts 0 → 1 → 2 → 3 → 4 → 5 → 0.

**Module Interface:**
```verilog
module mod6_counter(
    input  wire       clk,
    input  wire       rst,
    output reg  [2:0] count
);
```
""",
  "starter_code": """module mod6_counter(
    input  wire       clk,
    input  wire       rst,
    output reg  [2:0] count
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_mod6_counter;
    reg clk, rst; wire [2:0] count;
    integer i, failed = 0;
    mod6_counter uut (.clk(clk),.rst(rst),.count(count));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_mod6_counter);
        rst=1;#12;rst=0;
        for(i=0;i<6;i=i+1) begin
            if(count!==i) begin $display("FAILED: count=%0d expected %0d",count,i); failed=failed+1; end
            #10;
        end
        if(count!==0) begin $display("FAILED: should wrap to 0, got %0d",count); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Reset count when it reaches 5", "if(count==5) count<=0; else count<=count+1;"],
  "company_tags": ["Intel", "Qualcomm"],
},

{
  "title": "Ring Counter",
  "slug": "ring-counter",
  "difficulty": "medium",
  "category": "sequential",
  "description": """## 4-bit Ring Counter

Design a 4-bit ring counter. Only one bit is HIGH at a time and it rotates on each clock edge.

**Module Interface:**
```verilog
module ring_counter(
    input  wire       clk,
    input  wire       rst,
    output reg  [3:0] q
);
```

- Initial state after reset: q = 4'b0001
- Sequence: 0001 → 0010 → 0100 → 1000 → 0001
""",
  "starter_code": """module ring_counter(
    input  wire       clk,
    input  wire       rst,
    output reg  [3:0] q
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_ring_counter;
    reg clk, rst; wire [3:0] q;
    integer failed = 0;
    ring_counter uut (.clk(clk),.rst(rst),.q(q));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_ring_counter);
        rst=1;#12;rst=0;
        if(q!==4'b0001) begin $display("FAILED: init q=%b",q); failed=failed+1; end
        #10; if(q!==4'b0010) begin $display("FAILED: step1 q=%b",q); failed=failed+1; end
        #10; if(q!==4'b0100) begin $display("FAILED: step2 q=%b",q); failed=failed+1; end
        #10; if(q!==4'b1000) begin $display("FAILED: step3 q=%b",q); failed=failed+1; end
        #10; if(q!==4'b0001) begin $display("FAILED: wrap q=%b",q); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["q <= {q[2:0], q[3]};", "Initialize to 4'b0001 on reset"],
  "company_tags": ["AMD", "Intel"],
},

{
  "title": "Synchronous Up-Down Counter",
  "slug": "updown-counter",
  "difficulty": "medium",
  "category": "sequential",
  "description": """## Synchronous Up-Down Counter

Design a 4-bit synchronous up-down counter.

**Module Interface:**
```verilog
module updown_counter(
    input  wire       clk,
    input  wire       rst,
    input  wire       up,
    output reg  [3:0] count
);
```

- When up=1: count increments
- When up=0: count decrements
""",
  "starter_code": """module updown_counter(
    input  wire       clk,
    input  wire       rst,
    input  wire       up,
    output reg  [3:0] count
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_updown_counter;
    reg clk, rst, up; wire [3:0] count;
    integer failed = 0;
    updown_counter uut (.clk(clk),.rst(rst),.up(up),.count(count));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_updown_counter);
        rst=1;#12;rst=0;
        up=1;#10; if(count!==1) begin $display("FAILED: up count=%0d",count); failed=failed+1; end
        #10; if(count!==2) begin $display("FAILED: up count=%0d",count); failed=failed+1; end
        up=0;#10; if(count!==1) begin $display("FAILED: down count=%0d",count); failed=failed+1; end
        #10; if(count!==0) begin $display("FAILED: down count=%0d",count); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["if(up) count<=count+1; else count<=count-1;"],
  "company_tags": ["Qualcomm", "AMD"],
},

{
  "title": "Clock Divider",
  "slug": "clock-divider",
  "difficulty": "medium",
  "category": "sequential",
  "description": """## Clock Divider (Divide by 2)

Design a clock divider that outputs a clock with half the frequency of the input.

**Module Interface:**
```verilog
module clk_divider(
    input  wire clk,
    input  wire rst,
    output reg  clk_out
);
```

- clk_out toggles on every rising edge of clk
- After reset: clk_out = 0
""",
  "starter_code": """module clk_divider(
    input  wire clk,
    input  wire rst,
    output reg  clk_out
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_clk_divider;
    reg clk, rst; wire clk_out;
    integer failed = 0;
    clk_divider uut (.clk(clk),.rst(rst),.clk_out(clk_out));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_clk_divider);
        rst=1;#12;rst=0;
        if(clk_out!==0) begin $display("FAILED: should start 0"); failed=failed+1; end
        #10; if(clk_out!==1) begin $display("FAILED: should be 1 after 1 cycle"); failed=failed+1; end
        #10; if(clk_out!==0) begin $display("FAILED: should be 0 after 2 cycles"); failed=failed+1; end
        #10; if(clk_out!==1) begin $display("FAILED: should be 1 after 3 cycles"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Toggle clk_out on every posedge", "clk_out <= ~clk_out;"],
  "company_tags": ["Intel", "AMD", "Qualcomm"],
},

# ═══════════════════════════════════════════
# ADVANCED / VERIFICATION — 10 Problems
# ═══════════════════════════════════════════

{
  "title": "8-bit ALU",
  "slug": "alu-8bit",
  "difficulty": "hard",
  "category": "combinational",
  "description": """## 8-bit ALU

Design an 8-bit Arithmetic Logic Unit (ALU).

**Module Interface:**
```verilog
module alu_8bit(
    input  wire [7:0] a,
    input  wire [7:0] b,
    input  wire [2:0] op,
    output reg  [7:0] result,
    output reg        zero
);
```

**Operations:**
| op  | Operation      |
|-----|---------------|
| 000 | ADD (a + b)   |
| 001 | SUB (a - b)   |
| 010 | AND (a & b)   |
| 011 | OR  (a | b)   |
| 100 | XOR (a ^ b)   |
| 101 | NOT (~a)      |
| 110 | SHL (a << 1)  |
| 111 | SHR (a >> 1)  |

- zero=1 when result==0
""",
  "starter_code": """module alu_8bit(
    input  wire [7:0] a,
    input  wire [7:0] b,
    input  wire [2:0] op,
    output reg  [7:0] result,
    output reg        zero
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_alu_8bit;
    reg [7:0] a, b; reg [2:0] op; wire [7:0] result; wire zero;
    integer failed = 0;
    alu_8bit uut (.a(a),.b(b),.op(op),.result(result),.zero(zero));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_alu_8bit);
        a=8'd10;b=8'd5;op=3'b000;#10; if(result!==15) begin $display("FAILED: ADD"); failed=failed+1; end
        a=8'd10;b=8'd5;op=3'b001;#10; if(result!==5)  begin $display("FAILED: SUB"); failed=failed+1; end
        a=8'hF0;b=8'h0F;op=3'b010;#10; if(result!==0) begin $display("FAILED: AND"); failed=failed+1; end
        a=8'hF0;b=8'h0F;op=3'b011;#10; if(result!==8'hFF) begin $display("FAILED: OR"); failed=failed+1; end
        a=8'd5; b=8'd5; op=3'b000;#10; if(zero!==0) begin $display("FAILED: zero flag on 10"); failed=failed+1; end
        a=8'd5; b=8'd5; op=3'b001;#10; if(zero!==1) begin $display("FAILED: zero flag"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use case(op) statement", "Always block with always @(*)", "zero = (result == 0);"],
  "company_tags": ["Intel", "AMD", "Qualcomm", "NVIDIA"],
},

{
  "title": "PWM Generator",
  "slug": "pwm-generator",
  "difficulty": "hard",
  "category": "sequential",
  "description": """## PWM Generator

Design a Pulse Width Modulation (PWM) signal generator.

**Module Interface:**
```verilog
module pwm_gen(
    input  wire       clk,
    input  wire       rst,
    input  wire [7:0] duty,
    output wire       pwm_out
);
```

- duty: 0-255 sets duty cycle (0=0%, 255=100%)
- Uses an 8-bit counter internally
- pwm_out = 1 when counter < duty
""",
  "starter_code": """module pwm_gen(
    input  wire       clk,
    input  wire       rst,
    input  wire [7:0] duty,
    output wire       pwm_out
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_pwm_gen;
    reg clk, rst; reg [7:0] duty; wire pwm_out;
    integer high_count, total, failed;
    pwm_gen uut (.clk(clk),.rst(rst),.duty(duty),.pwm_out(pwm_out));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_pwm_gen);
        rst=1;#12;rst=0;
        duty=8'd128; high_count=0; total=256;
        repeat(256) begin #10; if(pwm_out) high_count=high_count+1; end
        if(high_count < 120 || high_count > 136) begin
            $display("FAILED: 50%% duty expected ~128 highs, got %0d", high_count);
            failed=failed+1;
        end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED");
        $finish;
    end
endmodule""",
  "hints": ["Use 8-bit counter that wraps 0-255",
            "assign pwm_out = (counter < duty);"],
  "company_tags": ["Qualcomm", "NVIDIA"],
},

{
  "title": "4-bit LFSR",
  "slug": "lfsr-4bit",
  "difficulty": "hard",
  "category": "sequential",
  "description": """## 4-bit Linear Feedback Shift Register (LFSR)

Design a 4-bit Fibonacci LFSR using taps at positions 4 and 3.

**Module Interface:**
```verilog
module lfsr_4bit(
    input  wire       clk,
    input  wire       rst,
    output reg  [3:0] q
);
```

- Feedback: bit = q[3] ^ q[2]
- On reset: q = 4'b0001
- Generates pseudo-random sequence of 15 unique values
""",
  "starter_code": """module lfsr_4bit(
    input  wire       clk,
    input  wire       rst,
    output reg  [3:0] q
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_lfsr_4bit;
    reg clk, rst; wire [3:0] q;
    integer failed = 0;
    reg [3:0] seen [0:15];
    integer i, unique;
    lfsr_4bit uut (.clk(clk),.rst(rst),.q(q));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_lfsr_4bit);
        rst=1;#12;rst=0;
        if(q!==4'b0001) begin $display("FAILED: init q=%b",q); failed=failed+1; end
        for(i=0;i<15;i=i+1) begin seen[i]=q; #10; end
        unique=0;
        for(i=0;i<15;i=i+1) if(seen[i]!==0) unique=unique+1;
        if(unique!==15) begin $display("FAILED: not 15 unique values"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["q <= {q[2:0], q[3]^q[2]};", "Reset to 4'b0001 (never 0)"],
  "company_tags": ["Intel", "Qualcomm", "AMD"],
},

{
  "title": "Debounce Circuit",
  "slug": "debounce-circuit",
  "difficulty": "hard",
  "category": "sequential",
  "description": """## Button Debounce Circuit

Design a digital debounce circuit that filters mechanical button bounce.

**Module Interface:**
```verilog
module debounce(
    input  wire clk,
    input  wire rst,
    input  wire btn,
    output reg  stable
);
```

- btn input may bounce (rapid 0/1 transitions)
- stable output should only change after btn is stable for 4 consecutive clock cycles
""",
  "starter_code": """module debounce(
    input  wire clk,
    input  wire rst,
    input  wire btn,
    output reg  stable
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_debounce;
    reg clk, rst, btn; wire stable;
    integer failed = 0;
    debounce uut (.clk(clk),.rst(rst),.btn(btn),.stable(stable));
    initial clk = 0;
    always #5 clk = ~clk;
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_debounce);
        rst=1;#12;rst=0;
        btn=0;#10;btn=1;#5;btn=0;#5;btn=1;#5;btn=0;#5;
        if(stable!==0) begin $display("FAILED: bounce should not change stable"); failed=failed+1; end
        btn=1;#50;
        if(stable!==1) begin $display("FAILED: stable btn=1 not detected"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use a counter that resets when btn changes",
            "Only update stable when counter reaches threshold"],
  "company_tags": ["Intel", "Qualcomm"],
},

{
  "title": "Priority Encoder 8:3",
  "slug": "priority-encoder-8to3",
  "difficulty": "medium",
  "category": "combinational",
  "description": """## 8:3 Priority Encoder

Design an 8-to-3 priority encoder. The highest active input gets encoded.

**Module Interface:**
```verilog
module priority_encoder(
    input  wire [7:0] in,
    output reg  [2:0] out,
    output reg        valid
);
```

- valid=1 when any input is HIGH
- out encodes the highest priority (highest bit) active input
""",
  "starter_code": """module priority_encoder(
    input  wire [7:0] in,
    output reg  [2:0] out,
    output reg        valid
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_priority_encoder;
    reg [7:0] in; wire [2:0] out; wire valid;
    integer failed = 0;
    priority_encoder uut (.in(in),.out(out),.valid(valid));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_priority_encoder);
        in=8'b00000000;#10; if(valid!==0) begin $display("FAILED: valid should be 0"); failed=failed+1; end
        in=8'b00000001;#10; if(out!==0||valid!==1) begin $display("FAILED: in[0]"); failed=failed+1; end
        in=8'b00000010;#10; if(out!==1||valid!==1) begin $display("FAILED: in[1]"); failed=failed+1; end
        in=8'b10000000;#10; if(out!==7||valid!==1) begin $display("FAILED: in[7]"); failed=failed+1; end
        in=8'b10000001;#10; if(out!==7||valid!==1) begin $display("FAILED: priority"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Use casez with wildcard bits",
            "Check from highest bit to lowest"],
  "company_tags": ["Intel", "AMD"],
},

{
  "title": "4-bit Ripple Carry Adder",
  "slug": "ripple-carry-adder",
  "difficulty": "medium",
  "category": "combinational",
  "description": """## 4-bit Ripple Carry Adder

Build a 4-bit ripple carry adder using full adder instances.

**Module Interface:**
```verilog
module ripple_carry_adder(
    input  wire [3:0] a,
    input  wire [3:0] b,
    input  wire       cin,
    output wire [3:0] sum,
    output wire       cout
);
```
""",
  "starter_code": """module full_adder(
    input  wire a, b, cin,
    output wire sum, cout
);
    assign sum  = a ^ b ^ cin;
    assign cout = (a&b)|(b&cin)|(a&cin);
endmodule

module ripple_carry_adder(
    input  wire [3:0] a,
    input  wire [3:0] b,
    input  wire       cin,
    output wire [3:0] sum,
    output wire       cout
);
    // Instantiate 4 full adders here

endmodule""",
  "testbench": """module tb_ripple_carry_adder;
    reg [3:0] a, b; reg cin; wire [3:0] sum; wire cout;
    integer failed = 0;
    ripple_carry_adder uut (.a(a),.b(b),.cin(cin),.sum(sum),.cout(cout));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_ripple_carry_adder);
        a=4'd5; b=4'd3; cin=0;#10;
        if(sum!==8||cout!==0) begin $display("FAILED: 5+3=%0d cout=%b",sum,cout); failed=failed+1; end
        a=4'd15;b=4'd1; cin=0;#10;
        if(sum!==0||cout!==1) begin $display("FAILED: 15+1 overflow"); failed=failed+1; end
        a=4'd7; b=4'd7; cin=1;#10;
        if({cout,sum}!==4'd7+4'd7+1) begin $display("FAILED: 7+7+1"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["Instantiate full_adder 4 times",
            "Chain carry outputs to carry inputs"],
  "company_tags": ["Intel", "Qualcomm", "AMD"],
},

{
  "title": "SR Latch",
  "slug": "sr-latch",
  "difficulty": "easy",
  "category": "sequential",
  "description": """## SR Latch (NOR-based)

Design an SR latch using NOR gates.

**Module Interface:**
```verilog
module sr_latch(
    input  wire s,
    input  wire r,
    output wire q,
    output wire qn
);
```

**Truth Table:**
| S | R | Q    | Qn   |
|---|---|------|------|
| 0 | 0 | Hold | Hold |
| 1 | 0 |  1   |  0   |
| 0 | 1 |  0   |  1   |
| 1 | 1 | Forbidden |
""",
  "starter_code": """module sr_latch(
    input  wire s,
    input  wire r,
    output wire q,
    output wire qn
);
    // Implement using NOR gates
    // assign q  = ~(r | qn);
    // assign qn = ~(s | q);

endmodule""",
  "testbench": """module tb_sr_latch;
    reg s, r; wire q, qn;
    integer failed = 0;
    sr_latch uut (.s(s),.r(r),.q(q),.qn(qn));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_sr_latch);
        s=1;r=0;#10; if(q!==1||qn!==0) begin $display("FAILED: SET q=%b",q); failed=failed+1; end
        s=0;r=0;#10; if(q!==1||qn!==0) begin $display("FAILED: HOLD after SET"); failed=failed+1; end
        s=0;r=1;#10; if(q!==0||qn!==1) begin $display("FAILED: RESET q=%b",q); failed=failed+1; end
        s=0;r=0;#10; if(q!==0||qn!==1) begin $display("FAILED: HOLD after RESET"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["assign q  = ~(r | qn);",
            "assign qn = ~(s | q);"],
  "company_tags": ["Intel", "Qualcomm"],
},

{
  "title": "2s Complement",
  "slug": "twos-complement",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## 2's Complement

Design a circuit that computes the 2's complement (negation) of an 8-bit number.

**Module Interface:**
```verilog
module twos_complement(
    input  wire [7:0] in,
    output wire [7:0] out
);
```

- out = -in in 2's complement representation
- Example: in=8'b00000001 → out=8'b11111111
""",
  "starter_code": """module twos_complement(
    input  wire [7:0] in,
    output wire [7:0] out
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_twos_complement;
    reg [7:0] in; wire [7:0] out;
    integer failed = 0;
    twos_complement uut (.in(in),.out(out));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_twos_complement);
        in=8'd1; #10; if(out!==8'hFF) begin $display("FAILED: ~1+1=%h",out); failed=failed+1; end
        in=8'd5; #10; if(out!==8'hFB) begin $display("FAILED: ~5+1=%h",out); failed=failed+1; end
        in=8'd0; #10; if(out!==8'h00) begin $display("FAILED: ~0+1=%h",out); failed=failed+1; end
        in=8'h80;#10; if(out!==8'h80) begin $display("FAILED: 2s of -128"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["assign out = ~in + 1;", "This is the definition of 2's complement"],
  "company_tags": ["Intel", "AMD"],
},

{
  "title": "Gray Code Converter",
  "slug": "gray-code-converter",
  "difficulty": "medium",
  "category": "combinational",
  "description": """## Binary to Gray Code Converter

Design a 4-bit binary to Gray code converter.

**Module Interface:**
```verilog
module gray_converter(
    input  wire [3:0] binary,
    output wire [3:0] gray
);
```

**Conversion:**
- gray[3] = binary[3]
- gray[2] = binary[3] ^ binary[2]
- gray[1] = binary[2] ^ binary[1]
- gray[0] = binary[1] ^ binary[0]
""",
  "starter_code": """module gray_converter(
    input  wire [3:0] binary,
    output wire [3:0] gray
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_gray_converter;
    reg [3:0] binary; wire [3:0] gray;
    integer failed = 0;
    gray_converter uut (.binary(binary),.gray(gray));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_gray_converter);
        binary=4'd0;#10; if(gray!==4'b0000) begin $display("FAILED: 0->%b",gray); failed=failed+1; end
        binary=4'd1;#10; if(gray!==4'b0001) begin $display("FAILED: 1->%b",gray); failed=failed+1; end
        binary=4'd2;#10; if(gray!==4'b0011) begin $display("FAILED: 2->%b",gray); failed=failed+1; end
        binary=4'd3;#10; if(gray!==4'b0010) begin $display("FAILED: 3->%b",gray); failed=failed+1; end
        binary=4'd7;#10; if(gray!==4'b0100) begin $display("FAILED: 7->%b",gray); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["assign gray = binary ^ (binary >> 1);",
            "Or assign each bit individually"],
  "company_tags": ["Intel", "AMD", "Qualcomm"],
},

{
  "title": "Parity Generator",
  "slug": "parity-generator",
  "difficulty": "easy",
  "category": "combinational",
  "description": """## Even Parity Generator

Design an 8-bit even parity generator.

**Module Interface:**
```verilog
module parity_gen(
    input  wire [7:0] data,
    output wire       parity
);
```

- parity=1 when number of 1s in data is odd (makes total even)
- parity=0 when number of 1s is even
""",
  "starter_code": """module parity_gen(
    input  wire [7:0] data,
    output wire       parity
);
    // Write your solution here

endmodule""",
  "testbench": """module tb_parity_gen;
    reg [7:0] data; wire parity;
    integer failed = 0;
    parity_gen uut (.data(data),.parity(parity));
    initial begin
        $dumpfile("waveform.vcd"); $dumpvars(0, tb_parity_gen);
        data=8'b00000000;#10; if(parity!==0) begin $display("FAILED: 0 ones"); failed=failed+1; end
        data=8'b00000001;#10; if(parity!==1) begin $display("FAILED: 1 one"); failed=failed+1; end
        data=8'b00000011;#10; if(parity!==0) begin $display("FAILED: 2 ones"); failed=failed+1; end
        data=8'b11111111;#10; if(parity!==0) begin $display("FAILED: 8 ones"); failed=failed+1; end
        data=8'b10101010;#10; if(parity!==0) begin $display("FAILED: 4 ones"); failed=failed+1; end
        if(failed==0) $display("All tests passed!");
        else $display("FAILED: %0d test(s) failed", failed);
        $finish;
    end
endmodule""",
  "hints": ["assign parity = ^data;", "XOR reduction operator"],
  "company_tags": ["Qualcomm", "Intel"],
},

]

# Seed all problems
for i, p in enumerate(problems):
    problem = Problem(
        title=p["title"],
        slug=p["slug"],
        difficulty=p["difficulty"],
        category=p["category"],
        description=p["description"],
        starter_code=p["starter_code"],
        testbench=p["testbench"],
        hints=p["hints"],
        company_tags=p["company_tags"],
    )
    db.add(problem)
    print(f"  ✅ Added: {p['title']}")

db.commit()
print(f"\n🎉 Successfully seeded {len(problems)} problems!")
db.close()
