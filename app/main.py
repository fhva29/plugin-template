from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get("/metadata")
def metadata():
    return {
        "name": "Example Plugin",
        "version": "1.0.0",
        "description": "This is an example plugin.",
        "developer": {"name": "Your Company", "contact_email": "you@example.com"},
        "frontend": {"url": "http://localhost:8000", "embed": True},
        "endpoints": [
            {"path": "/example", "methods": ["GET"], "description": "Example endpoint"}
        ],
        "auth_required": False,
    }


@app.get("/example")
def example():
    return {"message": "This is an example endpoint."}
