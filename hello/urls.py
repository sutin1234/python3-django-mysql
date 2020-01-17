from django.urls import path
from . import views  # import views.py

# defined url pattern
urlpatterns = [
    path('', views.index),
    path('index', views.index),
]
