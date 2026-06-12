from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.problem import Problem

router = APIRouter(prefix="/problems", tags=["problems"])

@router.get("/")
def list_problems(
    difficulty: str = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Problem)
    if difficulty:
        query = query.filter(Problem.difficulty == difficulty)
    if category:
        query = query.filter(Problem.category == category)
    problems = query.all()
    return [{
        "id": p.id, "title": p.title, "slug": p.slug,
        "difficulty": p.difficulty, "category": p.category,
        "company_tags": p.company_tags,
    } for p in problems]

@router.get("/{slug}")
def get_problem(slug: str, db: Session = Depends(get_db)):
    problem = db.query(Problem).filter(Problem.slug == slug).first()
    if not problem:
        raise HTTPException(404, "Problem not found")
    return {
        "id": problem.id, "title": problem.title,
        "difficulty": problem.difficulty, "category": problem.category,
        "description": problem.description,
        "starter_code": problem.starter_code,
        "hints": problem.hints,
        "company_tags": problem.company_tags,
    }
