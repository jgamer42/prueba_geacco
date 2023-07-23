from django.contrib import admin
from tasks.models import DomainTask, TaskPipeline, ListTasks
# Register your models here.


class DomainTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'document', 'task_type', 'start_at']
    list_filter = ['document', 'task_type']
    search_fields = ['id']


class TaskPipelineAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_at', 'end_at', 'document_format']
    list_filter = ['document_format']
    search_fields = ['id']


class StepAdmin(admin.ModelAdmin):
    list_display = ['id', 'step', 'task', 'pipeline']
    list_filter = ['pipeline']
    search_fields = ['id']


admin.site.register(DomainTask, DomainTaskAdmin)
admin.site.register(TaskPipeline, TaskPipelineAdmin)
admin.site.register(ListTasks, StepAdmin)
