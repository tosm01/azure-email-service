from django.urls import path

from . import views

urlpatterns = [
    path('v1/email', views.index, name='index'),
]