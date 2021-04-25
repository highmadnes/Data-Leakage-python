from django.db import models

# Create your models here.
class Registration(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Pass=models.CharField(max_length=20)
    role=models.IntegerField()
    status=models.IntegerField()
class Uploader(models.Model):
    Filename=models.CharField(max_length=50)
    fingerprint=models.CharField(max_length=100)
    userid=models.IntegerField()
    status=models.IntegerField()
class Request(models.Model):
    rabin=models.CharField(max_length=100)
    userid = models.CharField(max_length=10)
    status=models.IntegerField()
    checked=models.IntegerField()
