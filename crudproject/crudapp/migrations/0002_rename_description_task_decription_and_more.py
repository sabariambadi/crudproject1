# Generated by Django 4.2.2 on 2023-06-07 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='decription',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='priority',
            new_name='num',
        ),
    ]
