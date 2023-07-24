from django_celery_beat.models import PeriodicTask
from django.db import models
from src.constants import TASK_TYPES
from documents.models import DocumentFormat


class DomainTask(models.Model):
    task_type = models.CharField(max_length=10, choices=TASK_TYPES)
    document = models.ForeignKey(
        DocumentFormat, on_delete=models.DO_NOTHING, null=True)
    document_information = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    start_at = models.DateTimeField(blank=False)
    output_file = models.FileField(upload_to='files/output', blank=True)

    def __str__(self):
        return f'{self.task_type}-{self.document}'


class TaskPipeline(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    start_at = models.DateTimeField(blank=False)
    end_at = models.DateTimeField(blank=False)
    first_step = models.ForeignKey(
        DomainTask, on_delete=models.DO_NOTHING, related_name='start')
    end_step = models.ForeignKey(
        DomainTask, on_delete=models.DO_NOTHING, related_name='end')
    document_format = models.ForeignKey(
        DocumentFormat, on_delete=models.DO_NOTHING)
    output_file = models.FileField(upload_to='files/output', blank=True)

    def __str__(self):
        return f'{self.document_format}-{self.start_at}'


class ListTasks(models.Model):
    step = models.IntegerField(null=False)
    task = models.ForeignKey(
        DomainTask, on_delete=models.DO_NOTHING, null=True)
    pipeline = models.ForeignKey(
        TaskPipeline, on_delete=models.DO_NOTHING, null=True)
    is_last = models.BooleanField(null=False, default=False)

    class Meta:
        verbose_name = 'List task'
        verbose_name_plural = 'List tasks'
