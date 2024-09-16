install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black . 

test:
	python manage.py test documents/tests/

check:
	python manage.py check

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver		

all: install migration migrate check test format runserver

