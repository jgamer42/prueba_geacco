from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.TaskView.as_view()),
    path('result/<int:pk>', views.TaskView.as_view()),
    path('result/<int:pipeline_id>/<int:step>', views.StepView.as_view()),
]
