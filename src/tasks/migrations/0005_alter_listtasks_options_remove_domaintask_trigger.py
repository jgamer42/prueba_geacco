# Generated by Django 4.2.3 on 2023-07-23 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_listtasks_is_last'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listtasks',
            options={'verbose_name': 'List task',
                     'verbose_name_plural': 'List tasks'},
        ),
        migrations.RemoveField(
            model_name='domaintask',
            name='trigger',
        ),
    ]