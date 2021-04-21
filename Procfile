release: rm -rf db.sqlite3
release: python manage.py migrate
web: gunicorn reev.wsgi
