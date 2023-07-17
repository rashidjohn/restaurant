from django.urls import path
from .views import *

urlpatterns = [
    path('', contactView,  name='contact'),
    path('team/', teamView,  name='team'),
]
