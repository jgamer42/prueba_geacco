# Generated by Django 4.2.3 on 2023-07-23 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documents', '0002_alter_documentformat_original_file_delete_document'),
        ('django_celery_beat', '0018_improve_crontab_helptext'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[
                 ('GENERATE', 'GENERATE'), ('FILL', 'FILL')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_at', models.DateTimeField()),
                ('document', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='documents.documentformat')),
                ('document_information', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='documents.documentinformation')),
                ('trigger', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_celery_beat.periodictask')),
            ],
        ),
        migrations.CreateModel(
            name='TaskPipeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('output_file', models.FileField(
                    blank=True, upload_to='files/output')),
                ('document_format', models.ForeignKey(
                    on_delete=django.db.models.deletion.DO_NOTHING, to='documents.documentformat')),
                ('end_step', models.ForeignKey(
                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='end', to='tasks.domaintask')),
                ('first_step', models.ForeignKey(
                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='start', to='tasks.domaintask')),
            ],
        ),
        migrations.CreateModel(
            name='ListTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('pipeline', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.taskpipeline')),
                ('task', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.domaintask')),
            ],
        ),
    ]
