from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.DocumentsView.as_view()),
]