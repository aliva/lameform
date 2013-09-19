# init

    python2 manage.py syncdb --noinput
    python2 manage.py importdb <export.json>
    
# run

    python2 manage.py runserver
    firefox http://127.0.0.1:8000
    # user/pass = admin

tested with Python 2.7.5 and Django 1.5.4