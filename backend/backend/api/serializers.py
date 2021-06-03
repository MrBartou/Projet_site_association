from rest_framework import serializers
from .models import Events, Partnership, Subsciption

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('start', 'end', 'title')

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ('category', 'img_abs_path', 'title', 'description')

class SubsciptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsciption
        fields = ('fst_name', 'snd_name', 'mail', 'phone', 'school', 'promo')