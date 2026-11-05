install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test