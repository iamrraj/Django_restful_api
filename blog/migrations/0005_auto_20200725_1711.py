# Generated by Django 2.2.8 on 2020-07-25 15:11

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200630_1537'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blog',
            managers=[
                ('objects_unfiltered', django.db.models.manager.Manager()),
            ],
        ),
    ]
