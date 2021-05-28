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