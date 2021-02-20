

start:
	pipenv run gunicorn -w 2 -b 127.0.0.1:8080 myapp.app:flask_app


.PHONY: start
