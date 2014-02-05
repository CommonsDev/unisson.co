unisson.co
==========

Unisson website installation


apt-get install virtualenv

virtualenv --no-site-packages unisson-env

cd unisson-env

source bin/activate

git clone https://github.com/UnissonCo/unisson.co

cd unisson.co

pip install -r requirements.txt

python manage.py syncdb --all

python manage.py migrate --fake

python manage.py runserver
