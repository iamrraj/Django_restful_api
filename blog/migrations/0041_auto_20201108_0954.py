# Generated by Django 2.2.13 on 2020-11-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20201108_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Key for email tracking'),
        ),
    ]
