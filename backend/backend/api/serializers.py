from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Events

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'start', 'end', 'title', 'color', 'desc')

class PartenrshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('category', 'img_abs_path', 'title', 'description')

class SubsciptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('fst_name', 'snd_name', 'mail', 'phone', 'school', 'promo')