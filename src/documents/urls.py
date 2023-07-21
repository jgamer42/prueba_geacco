from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DocumentsView.as_view()),
    path("", views.DocumentsView.as_view()),
    path('<int:pk>', views.DocumentsDetailView.as_view()),
    path('fill/<int:pk>', views.FillDocument.as_view()),
]