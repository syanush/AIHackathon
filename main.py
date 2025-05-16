"""
Main entry point script for running the AIHackathon application.

This script starts both the FastAPI backend and Chainlit application
using multiprocessing to run them concurrently.
"""

import os
import sys
import subprocess
import multiprocessing
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)


def run_api():
    """Run the FastAPI backend server."""
    print("Starting FastAPI backend...")
    subprocess.run([
        "uvicorn", "app.api.app:app",
        "--host", "0.0.0.0",
        "--port", "8000",
        "--reload" if os.getenv("DEBUG", "False").lower() in ("true", "1", "t") else ""
    ])


def run_chainlit():
    """Run the Chainlit application."""
    print("Starting Chainlit application...")
    subprocess.run([
        "chainlit", "run", "app/app.py",
        "--host", "0.0.0.0",
        "--port", "8501"
    ])


def main():
    """Start both applications in separate processes."""
    # Create multiprocessing processes
    api_process = multiprocessing.Process(target=run_api)
    chainlit_process = multiprocessing.Process(target=run_chainlit)
    
    try:
        # Start processes
        api_process.start()
        chainlit_process.start()
        
        # Wait for processes to complete (they won't unless terminated)
        api_process.join()
        chainlit_process.join()
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        # Ensure processes are terminated
        if api_process.is_alive():
            api_process.terminate()
        if chainlit_process.is_alive():
            chainlit_process.terminate()


if __name__ == "__main__":
    main()
