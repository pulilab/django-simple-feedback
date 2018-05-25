# Installation

Install the pip package:

```bash
pip install django-simplefeedback
```

add 'simple-feedback' to INSTALLED_APPS

include 'simple-feedback.urls' into urlpatterns

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^api/", include("simple-feedback.urls")),
]
```

Migrate the db to crate simple-feedback models

```bash
python manage.py migrate
```

# Develop

Clone the repo

```bash
git clone git@github.com:pulilab/django-simple-feedback.git
```

## Test app

Test standalone app:

$ export DATABASE_URL='your_db'  # you can skip this, defaults to 'localhost' (use postgres.app for simplicity)

$ pip install -r requirements.txt

$ python runtests.py

## Run the app in develop mode

Create a new django project and install the package in develop mode

```bash
django-admin startproject simple_feedback_demo
cd simple_feedback_demo
pip install -e ~LOCAL_PATH_TO_DJANGO_SIMPLEFEEDBACK
```

Add `simple-feedback` to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simple-feedback'
]
```
Configure demo app urls

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^api/", include("simple-feedback.urls")),
]
```

Migrate db, create super user and run your demo app:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

open the browser at `http://localhost:8000/admin`

