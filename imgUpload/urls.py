from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'imageprocess', views.imageprocess, name='imageprocess')
]
