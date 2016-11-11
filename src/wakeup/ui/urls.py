from django.conf.urls import patterns, url
from ui import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]