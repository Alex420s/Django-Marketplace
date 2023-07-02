python3.9 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python manage.py makemigrations --noinput
python manage.py migrate --noinput

pip install -r requirements.txt
python manage.py collectstatic --noinput --clear