# Python-Django-Training

## Dependencies

+ Python 3.6.8
+ Django
+ MySql
 
## Setup Application

 + Take clone from repo
 + Create virtual environment and activate it.
    +  `virtualenv venv -p python3`
    + `source venv/bin/activate`
 + Install required packages
    + `pip install -r requirements.txt`
 + create `auth/local_settings.py` with your local database settings.
 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name', # Your local database name.
        'USER': 'db_user', # Your local database user e.g: root
        'PASSWORD': 'db_password', # Your local database password.
        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

+ Run Django localserver
    + `python manage.py runserver`