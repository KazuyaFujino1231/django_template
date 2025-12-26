# django_template

Minimal Django REST Framework template with a health check and echo API.

## Setup
    cd ~/work/django_template
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Run dev server
    source .venv/bin/activate
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000

## Sample API
- Health check: GET /api/health/ -> { status: ok }
- Echo: POST /api/echo/ (JSON body) -> { echo: <payload> }

Examples:
    curl http://localhost:8000/api/health/

## Tests
    source .venv/bin/activate
    python manage.py test

## Notes
- LANGUAGE_CODE=ja
- TIME_ZONE=Asia/Tokyo
- REST API renders/parses JSON only by default.
