
unisson.co
==========
Tools to support "Commons"

Join list discussion : http://unisson.co/group/unisson

Install App
==========

First, you need to setup an isolated developement environment for the
python apps using virtualenv_. If you don't have virtualenv_, you can
install it using your package manager such as *apt* if you're on
debian::

  apt-get install virtualenv
  virtualenv --no-site-packages unisson-env

Then, enters the environment::

  cd unisson-env
  source bin/activate
  
Your prompt should update to something like (note the prefix)::

  (i4p-env)glibersat@carpe:~/Source/unisson-env

.. warning::

  For all next steps, you need to be in an activated environment.
  
Getting the code
================

Once you're in your virtualenv directory, use::

  git clone https://github.com/UnissonCo/unisson.co
  cd unisson.co
  
fetch the dependencies using::

  pip install -r requirements.txt
  
*It may be the right to fetch a cup of coffee! :-)*

.. note::

  From now on, the ``unisson.co`` directory will be called **the project root** (or **PROJECT_ROOT**).


Populating the Database
=======================

You need to configure a database server (PostGreSQL_ is recommended,
see how to configure it in the :ref:`database-server-configuration`
section) and create a database for the project (such as
'imaginationforpeople').

.. warning::

   If you haven't configured your :file:`site_settings.py` yet, jump
   to :ref:`application-configuration` before going on.

Then you need to initialize your database with these commands::

    python manage.py syncdb --all
    python manage.py migrate --fake
    python manage.py check_permissions


Django will prompt for a user creation, this is always a good idea to say *yes*::

     You just installed Django's auth system, which means you don't have any superusers defined.
     Would you like to create one now? (yes/no): **yes**

Now, run the server :

   python manage.py runserver


Licenses
==========

This software is licensed under the AGPLv3 (See COPYING file for more information).

The media (pictures, sounds, videos, ...) are licensed under the Creative Commons CC-BY-SA (See MEDIA_COPYING for more information).
