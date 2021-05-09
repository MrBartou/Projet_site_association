from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Events

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'start', 'end', 'title', 'color', 'desc')