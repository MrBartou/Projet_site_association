from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r'^api/tutorials$', views.backend_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.backend_detail),
    url(r'^api/tutorials/published$', views.backend_list_published)
]