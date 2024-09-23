npm install
npm run build
python manage.py collectstatic --noinput
python manage.py migrate
