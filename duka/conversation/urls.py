from django.urls import path, include

from . import views

app_name = "conversation"

urlpatterns = [
    path('new/<int:item_pk>/', views.new, name="new"),
    path('', views.inbox, name="inbox"),
    path('<int:conversation_id>/', views.detail, name="detail"),
] 