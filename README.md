# Plugin Template for Wellnova

This is a template repository for creating a plugin compatible with the Wellnova platform.

> **Note:** This example is implemented in Python using FastAPI. However, plugins can be developed in **any language or framework**, as long as they:
>
> - Are packaged as a Docker image
> - Expose the required HTTP endpoints (`/healthcheck` and `/metadata`)
> - Follow the API and metadata conventions defined by Wellnova

## Available Endpoints in this Example

- `GET /healthcheck`: Plugin status check
- `GET /metadata`: Plugin metadata
- `GET /example`: Sample functionality endpoint

## Running Locally (Python example)

### 1. Create and activate virtual environment

```bash
uv venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
uv pip install --project .
```

### 3. Start the application

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker

If you're building with Docker, dependencies will be installed automatically from `pyproject.toml` using `uv`.

```bash
docker build -t plugin-example .
docker run -p 8000:8000 plugin-example
```
