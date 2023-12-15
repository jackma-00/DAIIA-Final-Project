.PHONY: venv install controller worker api

venv:
	python3 -m venv .venv

install:
	. ./.venv/bin/activate && \
	pip install --upgrade pip &&\
	pip install -r requirements.txt

controller:
	. .venv/bin/activate && \
	python -m fastchat.serve.controller

worker:
	. .venv/bin/activate && \
	python3 -m fastchat.serve.model_worker --model-path google/flan-t5-base

api:
	. .venv/bin/activate && \
	python -m fastchat.serve.openai_api_server --host localhost --port 8000

	
