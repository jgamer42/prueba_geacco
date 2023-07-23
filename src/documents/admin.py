from django.contrib import admin
from documents.models import DocumentFormat
# Register your models here.


class DocumentFormatAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'file_type']
    list_filter = ['file_type']
    search_fields = ['id']


admin.site.register(DocumentFormat, DocumentFormatAdmin)
