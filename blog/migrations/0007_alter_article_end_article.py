# Generated by Django 4.0.5 on 2022-06-22 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_end_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='end_article',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 14, 16, 30, 742883, tzinfo=utc)),
        ),
    ]
