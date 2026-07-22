
from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, users


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NorthStar IAM Platform",
    description="Enterprise-inspired identity and access management platform.",
    version="1.0.0",
)

app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {
        "application": "NorthStar IAM Platform",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
