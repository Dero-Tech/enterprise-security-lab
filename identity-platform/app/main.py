
from app.database import engine
from app.models.user import Base
from fastapi import FastAPI
from app.routers import users

app = FastAPI(
    title="NorthStar IAM Platform",
    version="1.0.0",
    description="Enterprise Identity and Access Management API"
)

Base.metadata.create_all(bind=engine)


app.include_router(users.router)


@app.get("/")
def home():
    return {
        "application": "NorthStar IAM Platform",
        "status": "Running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
