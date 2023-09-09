from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('lightcones/', views.lightcones, name='lightcones')
]