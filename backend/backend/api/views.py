from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class PartnershipViewSet(viewsets.ModelViewSet):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer

class SubsciptionViewSet(viewsets.ModelViewSet):
    queryset = Subsciption.objects.all()
    serializer_class = SubsciptionSerializer