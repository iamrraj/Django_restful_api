# Generated by Django 2.2.8 on 2020-08-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200802_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='8ef85605535fecb43d78', max_length=255, verbose_name='Key for email tracking'),
        ),
    ]
