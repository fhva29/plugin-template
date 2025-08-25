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
        "frontend": {
            "url": "http://localhost:8000",
            "embed": True,
        },
        "developer": {
            "name": "Dev Ltda",
            "contact_email": "dev@empresa.com",
        },
        "endpoints": [
            {
                "path": "/sum",
                "methods": ["POST"],
                "description": "Soma dois números",
                "request_schema": {
                    "type": "object",
                    "required": ["a", "b"],
                    "properties": {
                        "a": {
                            "type": "integer",
                            "description": "Primeiro número",
                        },
                        "b": {
                            "type": "integer",
                            "description": "Segundo número",
                        },
                    },
                },
            }
        ],
        "description": "Plugin de exemplo",
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
