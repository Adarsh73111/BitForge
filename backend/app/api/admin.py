from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.core.database import get_db
from app.models.problem import Problem
from app.core.config import settings

router = APIRouter(prefix="/admin", tags=["admin"])

# Simple admin key check
def verify_admin(x_admin_key: str = Header(...)):
    if x_admin_key != settings.SECRET_KEY:
        raise HTTPException(403, "Invalid admin key")
    return True

class ProblemCreate(BaseModel):
    title:        str
    slug:         str
    difficulty:   str
    category:     str
    description:  str
    starter_code: str
    testbench:    str
    hints:        List[str] = []
    company_tags: List[str] = []

class ProblemUpdate(BaseModel):
    title:        Optional[str] = None
    difficulty:   Optional[str] = None
    category:     Optional[str] = None
    description:  Optional[str] = None
    starter_code: Optional[str] = None
    testbench:    Optional[str] = None
    hints:        Optional[List[str]] = None
    company_tags: Optional[List[str]] = None

@router.get("/problems")
def list_all_problems(
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin)
):
    problems = db.query(Problem).all()
    return [{
        "id":         p.id,
        "title":      p.title,
        "slug":       p.slug,
        "difficulty": p.difficulty,
        "category":   p.category,
    } for p in problems]

@router.post("/problems", status_code=201)
def create_problem(
    req: ProblemCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin)
):
    if db.query(Problem).filter(Problem.slug == req.slug).first():
        raise HTTPException(400, "Slug already exists")
    problem = Problem(**req.dict())
    db.add(problem)
    db.commit()
    db.refresh(problem)
    return {"id": problem.id, "message": "Problem created successfully"}

@router.put("/problems/{problem_id}")
def update_problem(
    problem_id: int,
    req: ProblemUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin)
):
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(404, "Problem not found")
    for field, value in req.dict(exclude_none=True).items():
        setattr(problem, field, value)
    db.commit()
    return {"message": "Problem updated successfully"}

@router.delete("/problems/{problem_id}")
def delete_problem(
    problem_id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin)
):
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(404, "Problem not found")
    db.delete(problem)
    db.commit()
    return {"message": "Problem deleted successfully"}

@router.post("/problems/{problem_id}/test")
def test_problem(
    problem_id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin)
):
    """Test a problem's testbench with its own starter code"""
    from app.services.simulator import run_simulation
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(404, "Problem not found")
    result = run_simulation(
        user_code=problem.starter_code,
        testbench=problem.testbench,
    )
    return {
        "problem_id": problem_id,
        "title":      problem.title,
        "test_result": result["status"],
        "output":     result["output"],
    }
