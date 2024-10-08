# Exit on error
set -o errexit

pip install -r requirements.txt
npm install 
npm run build
python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput
python manage.py makemigrations --noinput