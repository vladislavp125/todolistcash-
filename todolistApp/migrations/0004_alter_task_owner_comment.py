# Generated by Django 5.1.1 on 2024-09-24 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0003_task_owner_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.CharField(default='anonim', max_length=50, verbose_name='Владелец'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255, verbose_name='Коментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='todolistApp.task')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
