# Generated by Django 4.2.3 on 2023-07-20 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('format', models.JSONField(blank=True)),
                ('file_type', models.CharField(choices=[('PDF', 'PDF'), ('DOCX', 'DOCX'), ('XLSX', 'XLSX'), ('PLAIN', 'PLAIN')], max_length=10)),
                ('original_file', models.FileField(blank=True, upload_to='files')),
                ('plain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payload', models.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_format', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='documents.documentformat')),
                ('payload', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='documents.documentinformation')),
            ],
        ),
    ]
