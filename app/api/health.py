"""Health check endpoints for the application."""

import os
import sys
import time
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.schemas import HealthCheck


router = APIRouter()


@router.get("/", response_model=HealthCheck)
async def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint to verify the application is running correctly.
    
    Returns:
        HealthCheck: Health check status
    """
    # Check database connection
    try:
        # Execute a simple query to check if the database is accessible
        db.execute("SELECT 1")
        db_connected = True
    except Exception as e:
        db_connected = False
        print(f"Database connection failed: {e}", file=sys.stderr)
    
    return HealthCheck(
        status="healthy",
        database_connected=db_connected
    )
