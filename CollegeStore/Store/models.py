from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.


class Department(models.Model):
    departmentname = models.CharField(max_length=250)

    def __str__(self):
        return self.departmentname


class Course(models.Model):
    deptid = models.ForeignKey(Department, on_delete=CASCADE)
    course = models.CharField(max_length=250)

    def __str__(self):
        return self.course

