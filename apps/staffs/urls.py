from django.urls import path

from . import views

urlpatterns = [
    path('staffs/', views.index, name='staffs'),
]