# Generated by Django 2.2.8 on 2020-08-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200802_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sent_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='sent at'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='10f134876a54caca9054', max_length=255, verbose_name='Key for email tracking'),
        ),
    ]