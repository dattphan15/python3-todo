# Run migrations with docker-compose up
python manage.py migrate --no-input

#  django by default overwrites your modified files on collectstatic command,
#  --noinput flag means it will not ask for your permission.
python manage.py collectstatic --no-input

gunicorn todo_list.wsgi:application --bind 0.0.0.0:8000