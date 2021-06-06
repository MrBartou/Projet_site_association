from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from backend.api import views

router = routers.DefaultRouter()
'''
event -> road for list event
partnership -> road for list partnership
subscription -> road for list subscription
admins -> road for list admins
'''
router.register(r'event', views.EventsViewSet)
router.register(r'partnership', views.PartnershipViewSet)
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