.PHONY: venv install format 

venv:
	python3 -m venv .venv

install: setup.py
	. ./.venv/bin/activate && \
	pip install --upgrade pip &&\
	pip install .[dev]

format:
	. ./.venv/bin/activate && \
	black .

run:
	. ./.venv/bin/activate && \
	python ./src/auction.py