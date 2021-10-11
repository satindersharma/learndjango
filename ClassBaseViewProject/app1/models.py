from django.db import models

# Create your models here.
class Employee(models.Model):
    POSTION_CHOICES = (
        ('mng', 'Manager'),
        ('dev', 'Devloper'),
        ('tst', 'Tester')
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    description = models.CharField(max_length=512, blank=True)
    position = models.CharField(max_length=3,
                                choices=POSTION_CHOICES,
                                default=POSTION_CHOICES[1][0])

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name