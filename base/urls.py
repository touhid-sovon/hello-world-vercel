from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view() , name='home'),
    path('about/', About.as_view() , name='about'),
]