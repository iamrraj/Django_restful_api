# Generated by Django 2.2.13 on 2020-10-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20201030_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='3ffc418ffb2b900c29b6', max_length=255, verbose_name='Key for email tracking'),
        ),
    ]