# Generated by Django 2.2.13 on 2020-10-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20201030_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='2b2977493eb69d241fbf', max_length=255, verbose_name='Key for email tracking'),
        ),
    ]