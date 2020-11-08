# Generated by Django 2.2.13 on 2020-10-30 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_forgottenpasswordtoken_success'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPasswordHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]