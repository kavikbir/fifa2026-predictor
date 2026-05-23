import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize environment defaults
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./fifa2026.db")

app = FastAPI(
    title="FIFA 2026 Predictor API",
    description="Backend API service for forecasting FIFA 2026 match outcomes, player stats, and group standings.",
    version="1.0.0",
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production for specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """
    Root endpoint containing basic API metadata.
    """
    return {
        "app": "FIFA 2026 Predictor API",
        "version": "1.0.0",
        "status": "online",
        "documentation": "/docs" if DEBUG else "unavailable"
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint for checking API availability and configuration status.
    """
    return {
        "status": "healthy",
        "database_configured": DATABASE_URL.startswith("sqlite") or len(DATABASE_URL) > 10,
        "debug_mode": DEBUG
    }
