from django.shortcuts import render
from django.http import JsonResponse
from tasks.tasks import generate_file
import datetime
from datetime import timedelta
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from rest_framework.generics import CreateAPIView
from dateutil import parser
# Create your views here.

class DocumentsView(CreateAPIView):
    def post(self,request):
        now = datetime.datetime.now()
        five_minutes_later = now + timedelta(minutes=5)
        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=five_minutes_later.minute,
            hour=five_minutes_later.hour,
            month_of_year=five_minutes_later.month,
            day_of_week=five_minutes_later.weekday(),
            periodictask=False
        )

        new_celery_task = PeriodicTask.objects.update_or_create(
            name=f"test task",
            defaults={
                "task": "tasks.tasks.generate_file",
                "args": [],
                "crontab": schedule,
            },
            start_time=five_minutes_later
        )
        return JsonResponse({"message":"task scheduled"})
