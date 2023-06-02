from django.urls import path, include

from . import views

app_name = "item"

urlpatterns = [
    path('', views.items, name="items"),
]