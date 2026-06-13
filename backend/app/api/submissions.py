from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.models.submission import Submission
from app.models.problem import Problem
from app.services.simulator import run_simulation
from app.services.vcd_parser import parse_vcd

router = APIRouter(prefix="/submissions", tags=["submissions"])

class SubmitRequest(BaseModel):
    problem_id: int
    code: str
    language: str = "verilog"

@router.post("/")
def submit(req: SubmitRequest, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.id == req.problem_id).first()
    if not problem:
        raise HTTPException(404, "Problem not found")

    submission = Submission(
        user_id=1,
        problem_id=req.problem_id,
        code=req.code,
        language=req.language,
        status="running"
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)

    # Run simulation
    result = run_simulation(
        user_code=req.code,
        testbench=problem.testbench,
        language=req.language,
    )

    # Parse VCD waveform
    waveform = None
    if result.get("vcd"):
        waveform = parse_vcd(result["vcd"])

    # Update submission
    submission.status     = result["status"]
    submission.result     = result["output"]
    submission.runtime_ms = result["runtime_ms"]
    db.commit()

    return {
        "submission_id": submission.id,
        "status":        result["status"],
        "output":        result["output"],
        "runtime_ms":    result["runtime_ms"],
        "waveform":      waveform,
    }

@router.get("/{submission_id}")
def get_submission(submission_id: int, db: Session = Depends(get_db)):
    sub = db.query(Submission).filter(Submission.id == submission_id).first()
    if not sub:
        raise HTTPException(404, "Submission not found")
    return {
        "id":         sub.id,
        "status":     sub.status,
        "result":     sub.result,
        "runtime_ms": sub.runtime_ms,
    }
