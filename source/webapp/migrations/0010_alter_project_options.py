# Generated by Django 4.1.6 on 2023-03-21 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_project_options_alter_status_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('add_user_project', 'Добавить пользователя в проект'), ('delete_user_project', 'Удалить пользователя из проекта')], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проект'},
        ),
    ]