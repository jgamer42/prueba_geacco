from django.db import models
from django.contrib.auth.models import User 
from src.constanst import DOCUMENT_TYPES


class DocumentFormat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    format = models.JSONField(blank=True)
    file_type=models.CharField(max_length=10,choices=DOCUMENT_TYPES)
    original_file = models.FileField(upload_to="files",blank=True)
    plain = models.TextField()


class DocumentInformation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    payload = models.JSONField(blank=True)



class Document(models.Model):
    document_format = models.ForeignKey("DocumentFormat",on_delete=models.DO_NOTHING)
    payload = models.ForeignKey("DocumentInformation",on_delete=models.DO_NOTHING)