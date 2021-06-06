from django.urls.base import reverse
from rest_framework.decorators import api_view
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.


@api_view(("GET",))
def api_root(request):
    return Response({
        "events": reverse('event-list', request=request),
        "partnerships": reverse('partnership-list', request=request),
        "subscriptions": reverse('subscription-list', request=request),
    })


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PartnershipViewSet(ModelViewSet):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (AllowGuestPostOnly,)
