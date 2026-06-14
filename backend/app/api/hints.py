from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.models.problem import Problem
from app.services.ai_hints import get_ai_hint

router = APIRouter(prefix="/hints", tags=["hints"])

class HintRequest(BaseModel):
    problem_id:   int
    user_code:    str
    error_output: str = ""
    hint_number:  int = 1

@router.post("/")
async def request_hint(req: HintRequest, db: Session = Depends(get_db)):
    if req.hint_number not in [1, 2, 3]:
        raise HTTPException(400, "hint_number must be 1, 2, or 3")

    problem = db.query(Problem).filter(Problem.id == req.problem_id).first()
    if not problem:
        raise HTTPException(404, "Problem not found")

    hint = await get_ai_hint(
        problem_title=problem.title,
        problem_description=problem.description,
        user_code=req.user_code,
        error_output=req.error_output,
        hint_number=req.hint_number,
    )

    return {
        "hint":        hint,
        "hint_number": req.hint_number,
        "problem_id":  req.problem_id,
    }
