from django.urls import path

from . import views

urlpatterns = [
    path('timeSheet/', views.index, name='timeSheet'),
]