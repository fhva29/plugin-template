from fastapi import FastAPI
from pydantic import BaseModel

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
            {"path": "/example", "methods": ["GET"], "description": "Example endpoint"},
            {
                "path": "/hello",
                "methods": ["GET"],
                "description": "Returns a greeting message",
            },
            {
                "path": "/sum",
                "methods": ["POST"],
                "description": "Receives two numbers and returns their sum",
            },
        ],
        "auth_required": False,
    }


@app.get("/hello")
def hello():
    return {"message": "Hello from the plugin!"}


class SumRequest(BaseModel):
    a: float
    b: float


@app.post("/sum")
def sum_numbers(data: SumRequest):
    return {"result": data.a + data.b}
