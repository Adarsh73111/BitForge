from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, problems, submissions, users, admin

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(problems.router)
app.include_router(submissions.router)
app.include_router(users.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"name": "BitForge API", "version": settings.VERSION, "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
