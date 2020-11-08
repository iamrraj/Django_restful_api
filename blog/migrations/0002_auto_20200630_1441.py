# Generated by Django 2.2.8 on 2020-06-30 12:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Blog1',
        ),
        migrations.AlterModelOptions(
            name='blog1',
            options={'verbose_name': 'blog1', 'verbose_name_plural': 'blogs1'},
        ),
    ]
