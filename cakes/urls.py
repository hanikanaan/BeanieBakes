from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('', views.list)
]
