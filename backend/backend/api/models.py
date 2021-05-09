from django.db import models

class Events(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    title = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)

# class Users(models.Users):
#     nom = models.CharField(max_length=256)
#     mail = models.CharField(max_length=256)
#     mdp = models.CharField(max_length=256)
#     token = models.CharField(max_length=256)
