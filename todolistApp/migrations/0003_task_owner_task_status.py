# Generated by Django 5.1.1 on 2024-09-23 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0002_alter_task_options_remove_task_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.CharField(default='anonim', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Черновик'), ('PUBLISHED', 'Опубликовано')], default='DRAFT', max_length=10, verbose_name='Статус'),
        ),
    ]
