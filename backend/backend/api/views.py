from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import EventsSerializer
from .models import Events

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer