from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    num = models.CharField(max_length=10, unique=True)
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
    seat_id = models.CharField(max_length=255, unique=True)
    seat_name = models.CharField(max_length=255, unique=True)

class Mystic(models.Model):
    mysitic_id = models.IntegerField(primary_key=True)
    student_id = models.IntegerField()
    tar_name = models.CharField(max_length=10)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    is_ok = models.BooleanField(default=0)
    mail = models.CharField(max_length=255)