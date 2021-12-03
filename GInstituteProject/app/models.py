from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=128)
    experience = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                              MaxValueValidator(50)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = "faculty"
        verbose_name = "Facutly"
        verbose_name_plural = "Facutlies"


class Course(models.Model):
    name = models.CharField(max_length=128)
    faculty = models.ManyToManyField(Faculty)
    discription = models.CharField(max_length=512, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "course"


class FeedBack(models.Model):
    name = models.CharField(max_length=128)
    comment = models.CharField(max_length=512)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "feedback"