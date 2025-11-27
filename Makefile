.PHONY: install test lint format run

install:
	pip install -r requirements.txt

test:
	pytest -v --cov=./

lint:
	flake8 .

format:
	black .

run:
	uvicorn main:app --host 0.0.0.0 --port 8000

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
