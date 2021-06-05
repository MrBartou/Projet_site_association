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
"""road to access subscription list"""
router.register(r'admins', views.AdminsViewSet)
"""road to access admin's login and management page"""

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^event/',views.activity_list),
    url(r'^users/',views.user_list),
    url(r'^partnerships/',views.partnership_list),
    url(r'events/(?P<title>[A-Z\-]+)$', views.suppr_acti),
]
"""describe patterns to access diferents roads"""