from django.db import models

class Events(models.Model):
    start = models.CharField(max_length=32)
    end = models.CharField(max_length=32)
    title = models.CharField(max_length=32)

class Partnership(models.Model):
    category = models.CharField(max_length=32)
    img_abs_path = models.CharField(max_length=256)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

class Subsciption(models.Model):
    fst_name = models.CharField(max_length=256)
    snd_name = models.CharField(max_length=256)
    mail = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    school = models.CharField(max_length=32)
    promo = models.CharField(max_length=4)

class Admins(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

# class Users(models.Users):
#     nom = models.CharField(max_length=256)
#     mail = models.CharField(max_length=256)
#     mdp = models.CharField(max_length=256)
#     token = models.CharField(max_length=256)