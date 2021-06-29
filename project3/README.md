`vitualenv geeta`

`geeta\Scripts\activate`

`pip freeze > requirements.txt`

`pip install -r requirements.txt`

`django-admin startproject project3`

`cd project3`

`python manage.py startapp demoapp`

## in `settings.py`

### add demoapp to `INSTALLED_APPS `

`mkdir templates`
### add template path `BASE_DIR / 'templates'`



### write model

```python

class Employee(models.Model):
    name = models.CharField(max_length=500)
    em_id  = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.em_id}"
```

### add to admin

```python
from django.contrib import admin
from .models import Employee
# Register your models here.


admin.site.register(Employee)

```


## try executing if else and another django template laguage