
# Functions From Zero

[![Python CI](https://github.com/sankardrbreaths/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/sankardrbreaths/functions-from-zero/actions/workflows/main.yml)

A hands-on Python project for learning software development, testing, CI/CD, Docker, and API deployment.

## Features

- Python functions and unit testing with pytest
- Code linting with Pylint and formatting with Black
- Command-line interfaces using Click
- REST API development using FastAPI
- Docker containerization
- Continuous Integration with GitHub Actions
- Wikipedia summary retrieval

## Run Locally

### Install dependencies

```bash
make install
```

### Run tests

```bash
make test
```

### Run linting

```bash
make lint
```

### Start FastAPI

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

API documentation: http://localhost:8000/docs

## Docker

Build the image:

```bash
docker build -t wiki-api:latest .
```

Run the container:

```bash
docker run --rm -p 8000:8000 wiki-api:latest
```

## Call the Microservice

### Wikipedia Summary API

**Endpoint:** `POST /predict`

```bash
curl -X POST \
  "https://curly-space-succotash-jjj44wrq59xq3rx-8000.app.github.dev/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Microsoft",
    "length": 10
  }'
```

Example response:

```json
{
  "summary": "Microsoft is an American multinational technology company..."
}
```

### Addition API

**Endpoint:** `GET /add/{a}/{b}`

```bash
curl http://localhost:8000/add/5/10
```

Response:

```json
{
  "sum": 15
}
```

## CI/CD Pipeline

GitHub Actions automatically runs the following checks:

1. Install project dependencies
2. Lint Python code
3. Run pytest tests
4. Check code formatting

[View GitHub Actions workflow](https://github.com/sankardrbreaths/functions-from-zero/actions/workflows/main.yml)

## Development

This repository is used for live training and experimentation with Python, MLOps, and software engineering best practices.
