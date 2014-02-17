unisson.co
==========
Tools to support "Commons"

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


Licenses
==========

This software is licensed under the AGPLv3 (See COPYING file for more information).

The media (pictures, sounds, videos, ...) are licensed under the Creative Commons CC-BY-SA (See MEDIA_COPYING for more information) to the exception of the files where the "Imagination For People" appears.
