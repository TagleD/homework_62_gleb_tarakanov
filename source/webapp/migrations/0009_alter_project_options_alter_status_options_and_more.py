# Generated by Django 4.1.6 on 2023-03-21 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_project_options_alter_status_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проект'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статус'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задача'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип задачи', 'verbose_name_plural': 'Тип задачи'},
        ),
    ]
