python manage.py migrate
python manage.py collectstatic --noinput
gunicorn project_peployement.wsgi:application --bind 0.0.0.0:$PORT