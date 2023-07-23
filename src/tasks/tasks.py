from celery import shared_task
from tasks.models import DomainTask, ListTasks
from django.core.files.base import ContentFile
from documents.helpers import write_file
from io import BytesIO


@shared_task(bind=True)
def generate_file(*args, **kwargs):
    current_id = args[1]
    task = DomainTask.objects.get(id=current_id)
    new_file = None
    if task.document.file_type != 'PLAIN':
        file = write_file(task.document.original_file.path,
                          task.document.file_type, task.document_information)
        file_buffer = BytesIO(file.read())
        new_file = ContentFile(
            file_buffer.read(), name=task.document.original_file.name.split('/')[-1])
    else:
        file = write_file(task.document.plain,
                          task.document.file_type, task.document_information)
        file_buffer = BytesIO(file.encode('utf-8'))
        file_name = 'salida.txt'
        new_file = ContentFile(file_buffer.read(), name=file_name)
    task.output_file = new_file
    task.save()
    current_step = ListTasks.objects.filter(task=task).first()
    if current_step.is_last:
        current_step.pipeline.output_file = file_buffer
        current_step.pipeline.save()
    return 1
