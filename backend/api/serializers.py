from rest_framework.serializers import *
from .models import Event, Partnership, Subscription


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'title',
            'start',
            'end',
        )


class PartnershipSerializer(ModelSerializer):
    class Meta:
        model = Partnership
        fields = (
            'category',
            'img_abs_path',
            'title',
            'description',
        )


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'first_name',
            'last_name',
            'event',
            'email_address',
            'phone_number',
            'school_name',
            'graduation_year',
        )
