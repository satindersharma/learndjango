from django.db import models

# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=500)
    em_id  = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.em_id}"