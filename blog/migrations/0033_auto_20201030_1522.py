# Generated by Django 2.2.13 on 2020-10-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20201023_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='d0840e4bfa6686511607', max_length=255, verbose_name='Key for email tracking'),
        ),
    ]