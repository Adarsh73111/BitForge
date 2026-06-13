from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.user import User
from app.models.submission import Submission

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{username}")
def get_profile(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(404, "User not found")

    # Get submission stats
    total = db.query(Submission).filter(Submission.user_id == user.id).count()
    passed = db.query(Submission).filter(
        Submission.user_id == user.id,
        Submission.status == "passed"
    ).count()

    # Unique problems solved
    solved = db.query(Submission.problem_id).filter(
        Submission.user_id == user.id,
        Submission.status == "passed"
    ).distinct().count()

    return {
        "id":              user.id,
        "username":        user.username,
        "email":           user.email,
        "problems_solved": solved,
        "total_submissions": total,
        "pass_rate":       round((passed/total*100) if total > 0 else 0, 1),
        "streak":          user.streak,
        "created_at":      str(user.created_at),
    }

@router.get("/")
def get_leaderboard(db: Session = Depends(get_db)):
    users = db.query(User).all()
    result = []
    for user in users:
        solved = db.query(Submission.problem_id).filter(
            Submission.user_id == user.id,
            Submission.status == "passed"
        ).distinct().count()
        result.append({
            "username":        user.username,
            "problems_solved": solved,
            "streak":          user.streak,
        })
    result.sort(key=lambda x: x["problems_solved"], reverse=True)
    return result[:50]
