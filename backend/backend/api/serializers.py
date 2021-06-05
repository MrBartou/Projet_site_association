"""Define what's contained in each element"""
from rest_framework import serializers
from .models import Events, Partnership, Subsciption, Admins

class EventsSerializer(serializers.ModelSerializer):
    """Event's definition"""
    class Meta:
        model = Events
        fields = ('start', 'end', 'title')

class PartnershipSerializer(serializers.ModelSerializer):
    """Partnership's definition"""
    class Meta:
        model = Partnership
        fields = ('category', 'img_abs_path', 'title', 'description')

class SubsciptionSerializer(serializers.ModelSerializer):
    """Subscription's definition"""
    class Meta:
        model = Subsciption
        fields = ('fst_name', 'snd_name', 'mail', 'phone', 'school', 'promo')

class AdminsSerializer(serializers.ModelSerializer):
    """Admin's's definition"""
    class Meta:
        model = Admins
        fields = ('username', 'email', 'password')