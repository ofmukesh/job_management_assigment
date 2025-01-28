# Variables
VENV_PATH = venv
PYTHON = $(VENV_PATH)/bin/python
PIP = $(VENV_PATH)/bin/pip
DJANGO_MANAGE = $(PYTHON) manage.py

# Default target
all: run

# Set up virtual environment and install dependencies
install:
	python3 -m venv $(VENV_PATH)
	$(PIP) install -r requirements.txt

# Run the Django development server
run:
	$(DJANGO_MANAGE) runserver

# Apply database migrations
migrate:
	$(DJANGO_MANAGE) makemigrations && $(DJANGO_MANAGE) migrate

# Create a superuser
createadmin:
	$(DJANGO_MANAGE) createsuperuser

# Collect static files
collectstatic:
	$(DJANGO_MANAGE) collectstatic --noinput

# Run tests
test:
	$(DJANGO_MANAGE) test

# Clean up __pycache__ and .pyc files
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

.PHONY: all install run migrate createadmin collectstatic test clean
