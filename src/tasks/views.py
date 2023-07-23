from django.http import JsonResponse
import datetime
from datetime import timedelta
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from rest_framework.generics import CreateAPIView
from tasks.models import TaskPipeline, DomainTask, ListTasks
from documents.models import DocumentFormat
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from tasks.validators import task_validator
from http import HTTPStatus
from django.db import transaction


class TaskView(CreateAPIView):
    @transaction.atomic
    def post(self, request):
        last_step_date = datetime.datetime.now()
        start_date = last_step_date
        payload = request.data
        if not task_validator.validate(request.data):
            print(task_validator.errors)
            return JsonResponse(task_validator.errors, status=HTTPStatus.BAD_REQUEST)

        doc_format = get_object_or_404(
            DocumentFormat, pk=request.data['document_format'])
        new_pipeline = TaskPipeline(
            start_at=start_date, document_format=doc_format)
        tasks_to_save = []
        steps_to_save = []
        for i, step in enumerate(payload['steps']):
            date_formatted = last_step_date + timedelta(**step['start'])
            schedule, _ = CrontabSchedule.objects.get_or_create(
                minute=date_formatted.minute,
                hour=date_formatted.hour,
                month_of_year=date_formatted.month,
                day_of_week=date_formatted.weekday(),
                periodictask=False
            )
            new_task = DomainTask(task_type=step['type'], document=doc_format, document_information=step.get(
                'payload'), start_at=date_formatted)
            new_step = ListTasks(step=i, task=new_task, pipeline=new_pipeline)
            if i >= len(payload['steps']):
                new_step.is_last = True
            new_task.save()
            new_celery_task, _ = PeriodicTask.objects.update_or_create(
                name=f'task-{new_task}-{new_task.start_at}',
                enabled=True,
                defaults={
                    'task': 'tasks.tasks.generate_file',
                    'args': [new_task.id],
                    'crontab': schedule
                },
                start_time=date_formatted
            )
            tasks_to_save.append(new_task)
            steps_to_save.append(new_step)
            last_step_date = date_formatted
        new_pipeline.end_at = last_step_date
        new_pipeline.end_step = tasks_to_save[-1]
        new_pipeline.first_step = tasks_to_save[0]
        new_pipeline.save()
        ListTasks.objects.bulk_create(steps_to_save)
        return JsonResponse({'message': 'task scheduled'})
