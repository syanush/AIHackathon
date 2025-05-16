"""Main FastAPI application entry point."""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api.health import router as health_router

# Load environment variables
load_dotenv()

# Get configuration from environment
API_PREFIX = os.getenv("API_PREFIX", "/api/v1")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

# Create FastAPI app
app = FastAPI(
    title="AIHackathon API",
    description="API for the AI Hackathon application",
    version="0.1.0",
    debug=DEBUG,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix=f"{API_PREFIX}/health", tags=["Health"])


@app.get("/")
async def root():
    """Root endpoint redirecting to API documentation."""
    return {
        "message": "Welcome to AIHackathon API",
        "documentation": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.api.app:app", host="0.0.0.0", port=8000, reload=DEBUG)
