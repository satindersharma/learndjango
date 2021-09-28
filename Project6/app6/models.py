from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    description = models.CharField(max_length=512,blank=True)

    def __str__(self):
        return self.name


        