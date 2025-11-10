.PHONY: run dev test docker

run:
	uvicorn app.main:app --reload --port 8000

test:
	pytest -q

docker:
	docker build -t churn-api:latest .
	docker run --rm -p 8000:8000 --env-file .env -v ${PWD}/models:/app/models:ro churn-api:latest
