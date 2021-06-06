from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
routes = (
    (r'events', EventViewSet),
    (r'partnerships', PartnershipViewSet),
    (r'subscriptions', SubscriptionViewSet),
)

for route, viewset in routes:
    router.register(route, viewset)

urlpatterns = (
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
)
