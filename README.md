# AI News Research & Summarizer

A full-stack research workspace for discovering news, comparing coverage across sources, and generating source-grounded summaries.

## Stack
- Python 3.12, Django REST Framework, JWT
- React + TypeScript + Vite
- PostgreSQL / SQLite development fallback
- News provider adapter and OpenAI-compatible summarization API
- Docker Compose and GitHub Actions CI

## Quick start
Copy `.env.example` to `.env`, configure provider keys, then run `docker compose up --build`.

Frontend: http://localhost:5173  
API: http://localhost:8000/api/  
Health: http://localhost:8000/api/health/

See the project structure and setup notes below. AI-generated output may omit nuance; follow source links and verify important claims against original reporting.
