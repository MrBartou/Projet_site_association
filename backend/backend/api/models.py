from django.db import models



class Events(models.Model):
    start = models.CharField(max_length=32)
    end = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)

class Partenrship(models.Model):
    category = models.CharField(max_length=32)
    img_abs_path = models.CharField(max_length=256)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

class Users(models.Users):
    nom = models.CharField(max_length=256)
    mail = models.CharField(max_length=256)
    mdp = models.CharField(max_length=256)
    token = models.CharField(max_length=256)