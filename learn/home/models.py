from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, default='Not Specified')
    phone_number = models.CharField(max_length=10)
    percentage = models.FloatField()
    student_bio = models.TextField()
    date_of_birth = models.DateField()
    registration = models.DateTimeField()
    # student_image = models.ImageField(upload_to= "images/students/")
    # student_file = models.FileField(upload_to= "file/students/")
    # created_at = models.DateTimeField(auto_now=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField()
    # uid = models.UUIDField()