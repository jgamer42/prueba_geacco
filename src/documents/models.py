from django.db import models
from src.constanst import DOCUMENT_TYPES


class DocumentFormat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    format = models.JSONField(blank=True)
    file_type = models.CharField(max_length=10, choices=DOCUMENT_TYPES)
    original_file = models.FileField(upload_to='files/formats', blank=True)
    plain = models.TextField()

    def __str__(self):
        return f'{self.file_type}-{self.original_file.name}'
