# Generated by Django 4.2.3 on 2023-07-23 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaintask',
            name='document_information',
            field=models.JSONField(),
        ),
    ]