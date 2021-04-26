from django.urls import path
from .views import *

app_name = 'MotorTest'

urlpatterns = [
    path('getVersion/', getVersion),
    path('feedback/', feedback),
    path('sendTestResult/', sendTestResult),
]