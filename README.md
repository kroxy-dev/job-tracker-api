# Job Application Tracker API

A REST API for tracking job applications, built with FastAPI and SQLite.

## Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Setup

1. Clone the repo

git clone https://github.com/kroxy-dev/job-tracker-api
cd job-tracker-api

2. Install dependencies

pip install fastapi uvicorn sqlalchemy

3. Run the server

uvicorn main:app --reload

4. Open the interactive docs at http://127.0.0.1:8000/docs

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| GET | /applications | Get all applications |
| POST | /applications | Add a new application |
| PUT | /application/{id} | Update an application |
| DELETE | /application/{id} | Delete an application |

## Request Body (POST and PUT)

{
  "company": "Google",
  "position": "Backend Developer",
  "status": "applied",
  "notes": "referral from friend"
}