from django.db import models

# Create your models here.


class datetime1(models.Model):
    time12 = models.TextField(max_length=255)
    class Meta:
        db_table="datetime1"


class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    comment = models.TextField(max_length=255)
    class Meta:
           db_table="contactus"


class reguser(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    password = models.TextField(max_length=255)
    class Meta:
        db_table="reguser"


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

