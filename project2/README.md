# Project2


`django-admin startproject project2`



`You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.`  

contrib packages¶

Django aims to follow Python’s “batteries included” philosophy. It ships with a variety of extra, optional tools that solve common Web-development problems.




```bash
pip install virtualenv
```


```bash
virtualenv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install Django

```

```bash

pip freeze > requirements.txt
```
#### Migrate to add to database
```bash
python manage.py migrate
```

#### Create a Super user

```bash
python manage.py createsuperuser
```




```bash
deactivate
```



### Create new app

#### provide your choice of appname
```bash

python manage.py startapp app_name
```
#### eg.
```bash

python manage.py startapp newapp

```
## Now go to main project settings.py

and add new app to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nwaapp',# new app
]
```


## how to create new model

### go to `models.py`

### Write a class which inhereit `models.Model`
### Eg.

```python
class Employee(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

```

## how to add a Model in admin panel

### go to admin.py 

```python

from .models import Employee

admin.site.register(Employee)

```




