from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from backend.api import views

router = routers.DefaultRouter()
router.register(r'event', views.EventsViewSet)
router.register(r'partnership', views.PartnershipViewSet)
router.register(r'subscription', views.SubsciptionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]