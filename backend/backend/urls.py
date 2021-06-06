"""URL path and rules to access backend elements"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from backend.api import views

router = routers.DefaultRouter()

router.register(r'event', views.EventsViewSet)
"""road to access event list"""
router.register(r'partnership', views.PartnershipViewSet)
"""road to access partnership list"""
router.register(r'subscription', views.SubsciptionViewSet)
router.register(r'admins', views.AdministratorsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^event/',views.activity_list),
    url(r'^users/',views.user_list),
    url(r'^partnerships/',views.partnership_list),
    url(r'events/(?P<title>[A-Za-z0-9_. ]+)$', views.suppr_acti),
]
