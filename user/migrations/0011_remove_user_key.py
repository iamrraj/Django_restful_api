# Generated by Django 2.2.8 on 2020-10-23 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20201023_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='key',
        ),
    ]
