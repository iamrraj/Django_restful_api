# Generated by Django 2.2.13 on 2020-09-11 17:50

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0021_auto_20200904_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='7bcd1529a9a613a8d588', max_length=255, verbose_name='Key for email tracking'),
        ),
        migrations.CreateModel(
            name='BlogPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description about image')),
                ('file', models.FileField(blank=True, max_length=500, null=True, upload_to=blog.models.generic_upload_blog, verbose_name='Upload documents image')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='blog')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
