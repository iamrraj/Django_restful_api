# Generated by Django 2.2.8 on 2020-08-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200727_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deleted at'),
        ),
        migrations.AddField(
            model_name='blog',
            name='post_like',
            field=models.IntegerField(default='0', verbose_name='Total Like on post'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='a4144719030dec6a157b', max_length=255, verbose_name='Key for email tracking'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default='0', verbose_name='Total views on post'),
        ),
    ]
