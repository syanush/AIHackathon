# AIHackathon

A starter project for an AI hackathon featuring Chainlit for the conversational interface and PostgreSQL for data storage. This project includes a complete CI/CD pipeline with automated deployment to Render.com.

## Features

- 🤖 Chainlit conversational interface
- 🗃️ PostgreSQL database with SQLAlchemy ORM
- 🐳 Docker Compose for local development
- 🔄 GitHub Actions CI/CD pipeline
- 🚀 Automated deployment to Render.com
- 🔍 Health check endpoints and database connection testing

## Getting Started

### Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Git

### Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/AIHackathon.git
cd AIHackathon
```

2. **Set up a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create environment file**

```bash
cp .env.template .env
# Edit .env with your desired configuration
```

5. **Start the PostgreSQL database**

```bash
docker-compose up -d
```

6. **Test the database connection**

```bash
python scripts/test_db.py
```

7. **Create a favicon (optional)**

```bash
python scripts/create_favicon.py
```

8. **Run the application**

```bash
python main.py
```

The application will be available at:
- Chainlit UI: http://localhost:8501
- API (FastAPI): http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Docker Setup (Alternative)

You can run the entire application stack using Docker Compose:

```bash
# This will be implemented in a future update
```

## Project Structure

```
AIHackathon/
├── .env.template          # Environment variables template
├── .github/               # GitHub Actions workflows
├── app/                   # Main application code
│   ├── api/               # API endpoints
│   ├── app.py             # Chainlit app
│   ├── database/          # Database connection and utilities
│   ├── models/            # Data models and schemas
│   ├── static/            # Static files
│   └── utils/             # Utility functions
├── docker-compose.yml     # Docker Compose configuration
├── main.py                # Main entry point
├── render.yaml            # Render.com deployment configuration
├── requirements.txt       # Python dependencies
└── scripts/               # Utility scripts
    └── database/          # Database initialization scripts
```

## Deployment

The project is configured for automatic deployment to Render.com. When you push changes to the main branch, GitHub Actions will run tests and trigger a deployment to Render.com.

### Setup with Render.com

1. Create an account on Render.com
2. Create a new Blueprint instance pointing to your GitHub repository
3. Add the following secrets to your GitHub repository:
   - RENDER_API_KEY: Your Render API key
   - RENDER_SERVICE_ID: The ID of your Render service
   - RENDER_EXTERNAL_URL: The URL of your deployed application

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
