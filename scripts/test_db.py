"""
Test database connection and initialize tables.
"""

import os
import sys
from sqlalchemy import text

# Adjust path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.connection import engine, Base
from app.models.models import User, Conversation, Message


def test_connection():
    """Test database connection and create tables."""
    try:
        # Test connection by executing a simple query
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Database connection successful!")
            
            # Create all tables
            print("Creating database tables...")
            Base.metadata.create_all(bind=engine)
            print("Tables created successfully!")
            
            # Get table names
            table_names = engine.table_names()
            print(f"Tables in database: {', '.join(table_names)}")
            
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)


if __name__ == "__main__":
    test_connection()
