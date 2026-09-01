# GAMEVERSE Automation Makefile

.PHONY: install seed test test-backend build-frontend run-backend run-frontend docker-up docker-down clean

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

seed:
	python -m backend.app.seeds.seed_runner

test:
	pytest backend/tests -v

build-frontend:
	cd frontend && npm run build

run-backend:
	uvicorn app.main:app --app-dir backend --host 0.0.0.0 --port 8000 --reload

run-frontend:
	cd frontend && npm run dev

docker-up:
	docker-compose up --build -d

docker-down:
	docker-compose down

clean:
	rm -rf backend/__pycache__ backend/app/**/__pycache__ frontend/dist frontend/node_modules
