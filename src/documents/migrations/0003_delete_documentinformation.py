# Generated by Django 4.2.3 on 2023-07-23 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_domaintask_document_information'),
        ('documents', '0002_alter_documentformat_original_file_delete_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DocumentInformation',
        ),
    ]
