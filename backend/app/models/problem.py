from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Problem(Base):
    __tablename__ = "problems"

    id            = Column(Integer, primary_key=True, index=True)
    title         = Column(String, nullable=False)
    slug          = Column(String, unique=True, index=True, nullable=False)
    difficulty    = Column(String, nullable=False)  # easy/medium/hard
    category      = Column(String, nullable=False)  # combinational/sequential/verification
    description   = Column(Text, nullable=False)
    starter_code  = Column(Text, nullable=False)
    testbench     = Column(Text, nullable=False)
    hints         = Column(JSON, default=[])
    company_tags  = Column(JSON, default=[])
    created_at    = Column(DateTime(timezone=True), server_default=func.now())
