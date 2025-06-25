FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Atualiza pip e instala build dependencies
RUN pip install --upgrade pip setuptools wheel

# Instala o próprio projeto e suas dependências (lê o pyproject.toml)
RUN pip install .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
