from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('list', views.list)
]