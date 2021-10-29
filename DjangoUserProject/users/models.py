from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    GENDER_CHOICE = (('M','Male'),
                    ('F','Female'),
                    ('O','Other'))
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'