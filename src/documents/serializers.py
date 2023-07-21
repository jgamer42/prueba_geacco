from rest_framework import serializers
from documents.models import DocumentFormat

class DocumentFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFormat
        fields = ['id', 'created_at', 'file_type', 'format']