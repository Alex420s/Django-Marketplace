# Exit on error
set -o errexit


python manage.py collectstatic --noinput 
python manage.py migrate --noinput
python manage.py makemigrations --noinput
