# Generated by Django 4.2.3 on 2023-07-23 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentformat',
            name='original_file',
            field=models.FileField(blank=True, upload_to='files/formats'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]