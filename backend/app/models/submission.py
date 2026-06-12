from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Submission(Base):
    __tablename__ = "submissions"

    id          = Column(Integer, primary_key=True, index=True)
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=False)
    problem_id  = Column(Integer, ForeignKey("problems.id"), nullable=False)
    code        = Column(Text, nullable=False)
    language    = Column(String, default="verilog")  # verilog / systemverilog
    status      = Column(String, default="pending")  # pending/running/passed/failed/error
    result      = Column(Text, nullable=True)
    waveform_url = Column(String, nullable=True)
    runtime_ms  = Column(Integer, nullable=True)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
