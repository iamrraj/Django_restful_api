# Generated by Django 2.2.8 on 2020-08-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200802_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='key',
            field=models.CharField(default='53f278499cb1cc1aa727', max_length=255, verbose_name='Key for email tracking'),
        ),
        migrations.CreateModel(
            name='FavoriteBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_blog', models.ManyToManyField(blank=True, related_name='favorite', to='blog.Blog')),
            ],
            options={
                'verbose_name': 'favorite',
                'verbose_name_plural': 'favorites',
            },
        ),
    ]
