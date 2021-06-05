"""Define each elements in backend"""
from django.db import models

class Events(models.Model):
    """Event class describe what's contained in a calendar event"""
    start = models.CharField(max_length=32)
    """start date of an event"""
    end = models.CharField(max_length=32)
    """end date of an event"""
    title = models.CharField(max_length=32)
    """Event's name"""


class Partnership(models.Model):
    """Partneship class describe what's contained in a partnership poster"""
    category = models.CharField(max_length=32)
    """type of the partnership (food, sport, etc.)"""
    img_abs_path = models.CharField(max_length=256)
    """path where the image is stored"""
    title = models.CharField(max_length=32)
    """name of the partner"""
    description = models.CharField(max_length=256)
    """description of the partnership"""

class Subsciption(models.Model):
    """Subscribtion class describe what's contained in a subscription form"""
    fst_name = models.CharField(max_length=256)
    """first name of the new subscriber"""
    snd_name = models.CharField(max_length=256)
    """second name of the new subscriber"""
    mail = models.CharField(max_length=256)
    """email of the new subscriber"""
    phone = models.CharField(max_length=32)
    """phone number of the new subscriber"""
    school = models.CharField(max_length=32)
    """formation type of the new subscriber (IT, digital, mscPro)"""
    promo = models.CharField(max_length=4)
    """promotion year of the new subscriber (2025, 2024, etc.)"""

class Admins(models.Model):
    """Admin class describe what describe an admin"""
    username = models.CharField(max_length=32)
    """admin's username"""
    email = models.CharField(max_length=32)
    """admin's email"""
    password = models.CharField(max_length=32)
    """admin's password"""