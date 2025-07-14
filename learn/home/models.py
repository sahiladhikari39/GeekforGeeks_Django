from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=2)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, default='Not Specified')
    phone_number = models.CharField(max_length=10)
    percentage = models.FloatField()
    student_bio = models.TextField()
    date_of_birth = models.DateField()
    registration = models.DateTimeField()