"""
Seed the database with the first BitForge problem.
"""
from app.core.database import SessionLocal
from app.models.problem import Problem

db = SessionLocal()

# Check if already seeded
if db.query(Problem).count() > 0:
    print("✅ Problems already seeded")
    db.close()
    exit()

problem = Problem(
    title="AND Gate",
    slug="and-gate",
    difficulty="easy",
    category="combinational",
    description="""## AND Gate

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
    starter_code="""module and_gate(
    input  wire a,
    input  wire b,
    output wire y
);
    // Write your solution here
    
endmodule""",
    testbench="""module tb_and_gate;
    reg a, b;
    wire y;
    integer failed = 0;

    and_gate uut (.a(a), .b(b), .y(y));

    initial begin
        $dumpfile("waveform.vcd");
        $dumpvars(0, tb_and_gate);

        a=0; b=0; #10;
        if (y !== 0) begin $display("FAILED: 0 AND 0 = %b (expected 0)", y); failed=failed+1; end

        a=0; b=1; #10;
        if (y !== 0) begin $display("FAILED: 0 AND 1 = %b (expected 0)", y); failed=failed+1; end

        a=1; b=0; #10;
        if (y !== 0) begin $display("FAILED: 1 AND 0 = %b (expected 0)", y); failed=failed+1; end

        a=1; b=1; #10;
        if (y !== 1) begin $display("FAILED: 1 AND 1 = %b (expected 1)", y); failed=failed+1; end

        if (failed == 0)
            $display("All tests passed!");
        else
            $display("FAILED: %0d test(s) failed", failed);

        $finish;
    end
endmodule""",
    hints=["Use the & operator", "Verilog: assign y = a & b;"],
    company_tags=["Intel", "Qualcomm"],
)

db.add(problem)
db.commit()
print("✅ AND Gate problem seeded successfully!")
db.close()
