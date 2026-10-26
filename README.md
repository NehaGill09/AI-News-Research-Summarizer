# AI News Research & Summarizer

A full-stack research workspace for discovering news, comparing coverage across sources, and generating source-grounded summaries. The UI is branded **SignalDesk**.

## Architecture
- **Backend:** Python 3.12, Django 5, Django REST Framework, SimpleJWT
- **Frontend:** React, TypeScript, Vite, Lucide icons
- **Database:** PostgreSQL via Docker Compose; SQLite for local development
- **Providers:** NewsAPI-compatible search and OpenAI-compatible chat completions
- **Quality:** Django API tests and GitHub Actions CI

## Features
- Topic-based news discovery and canonical-URL deduplication
- Short and detailed article summaries with key takeaways and caveats
- Multi-source research report endpoint that retains source URLs and dates
- JWT token and refresh endpoints; per-user saved article API
- Responsive dashboard with search, source filters, saved stories, and article links
- Rate limiting, CORS configuration, health endpoint, and environment-based secrets
- Extractive fallback summaries when no AI key is configured

## Run with Docker
1. Create a local env file: `cp .env.example .env` (Windows: copy the file manually).
2. Add your provider keys if you want live search and model-generated summaries.
3. Start the stack: `docker compose up --build`.
4. Open the dashboard at http://localhost:5173 and API at http://localhost:8000/api/.

Health check: http://localhost:8000/api/health/

## Local development
Backend:
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Frontend in another terminal:
```bash
cd frontend
npm install
npm run dev
```

## API endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health/` | API and database health |
| GET | `/api/news/search/?q=...` | Search provider articles |
| POST | `/api/research/summarize/` | Summarize one article |
| POST | `/api/research/report/` | Synthesize up to 20 supplied articles |
| POST / GET | `/api/saved/` | Create/list authenticated saved articles |
| DELETE | `/api/saved/<id>/` | Remove a saved article |
| POST | `/api/auth/token/` | Obtain JWT tokens |
| POST | `/api/auth/refresh/` | Refresh access token |

Summarize request example:
```json
{"title":"Example headline","content":"Article text goes here.","url":"https://example.com/story","mode":"brief"}
```

## Configuration
See `.env.example`. Never commit real API keys. Live discovery requires `NEWS_API_KEY`; AI summaries require `AI_API_KEY` and an OpenAI-compatible endpoint. Without an AI key, the backend uses an extractive fallback. The dashboard's included demo stories are illustrative placeholders, not live reporting.

## Testing
```bash
cd backend && python manage.py test
cd frontend && npm install && npm run build
```

## Responsible use
Summaries may omit context or misstate nuance. The service keeps source links and explicitly returns limitations; verify consequential claims in original reporting. Respect provider terms, copyright, and rate limits when collecting news.

## Roadmap
- Celery/Redis background refresh and scheduled digests
- Topic workspaces, report export, semantic story clustering
- Integration tests with mocked provider responses
- Deployment manifests and observability

## License
MIT
