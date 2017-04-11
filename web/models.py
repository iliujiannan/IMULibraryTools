from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    num = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    class_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)

class Search(models.Model):
    search_id = models.IntegerField(primary_key=True)
    student_id = models.IntegerField()
    name = models.CharField(max_length=30)
    search_time = models.CharField(max_length=255)

class Subscribe(models.Model):
    subscribe_id = models.IntegerField(primary_key=True)
    student_id = models.IntegerField()
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)

class Seat(models.Model):
    id = models.IntegerField(primary_key=255)
    seat_id = models.CharField(max_length=255)
    seat_name = models.CharField(max_length=255)