# World Data Browser

## This is a small project that aims at providing info about continents, regions, countries, cities and more.

### To run the project

* Create a virtualenv to work in
* In the virtualenv install all the necessary libraries: ```pip install -r requirements.txt```
* Create a local_settings.py file in the **world_exercise** folder
* These local settings should at least hold SECRET_KEY, DEBUG and DATABASE settings tailored to your needs, for example:


```python
#this can be retrieved from environment variables
# here it's plaintext in a non-versioned local file
SECRET_KEY = '#gn@rpjy&n%#_dh-1zv**&f)r3)y=jw_gkkezom$-iz5k@eiaru'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '',
        'PORT': '',
        'NAME': 'iqvia',
        'USER': 'mikolaj',
        'PASSWORD': 'admin',
    },
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```


* Of course you need to create the database beforehand
* You need to run migrations: `./manage.py migrate`
* Then to load fixtures (world data): `./manage.py loaddata initial_world_data.json`
* Run the server and visit for example `http://127.0.0.1:8000/world/api/city/` for data preview

* Next step is the setup of the front end side, described in the README of a sister project:
