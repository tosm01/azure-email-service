from django.urls import path
from .views import EmailAPI

urlpatterns = [
    path('v1/email', EmailAPI.as_view(), name='sendEmail'),
]
