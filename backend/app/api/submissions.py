from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.models.submission import Submission

router = APIRouter(prefix="/submissions", tags=["submissions"])

class SubmitRequest(BaseModel):
    problem_id: int
    code: str
    language: str = "verilog"

@router.post("/")
def submit(req: SubmitRequest, db: Session = Depends(get_db)):
    submission = Submission(
        user_id=1,  # placeholder until auth middleware added
        problem_id=req.problem_id,
        code=req.code,
        language=req.language,
        status="pending"
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return {"submission_id": submission.id, "status": "pending"}

@router.get("/{submission_id}")
def get_submission(submission_id: int, db: Session = Depends(get_db)):
    sub = db.query(Submission).filter(Submission.id == submission_id).first()
    if not sub:
        raise HTTPException(404, "Submission not found")
    return {
        "id": sub.id, "status": sub.status,
        "result": sub.result, "waveform_url": sub.waveform_url,
        "runtime_ms": sub.runtime_ms,
    }
