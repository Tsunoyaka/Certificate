run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

restartdb:
	dropdb certificate_db
	createdb certificate_db
	python3 manage.py makemigrations account
	python3 manage.py makemigrations certificates
	python3 manage.py migrate
	python3 manage.py createsuperuser

