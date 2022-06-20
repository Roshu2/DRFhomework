# Generated by Django 4.0.5 on 2022-06-20 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_end_article_article_show_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='end_article',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 8, 56, 11, 100598, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='show_article',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 6, 20, 8, 56, 11, 100598, tzinfo=utc)),
        ),
    ]
