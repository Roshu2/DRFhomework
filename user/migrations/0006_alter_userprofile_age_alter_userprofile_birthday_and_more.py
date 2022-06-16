# Generated by Django 4.0.5 on 2022-06-16 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_userprofile_hobby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(verbose_name='생일'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hobby',
            field=models.ManyToManyField(to='user.hobby', verbose_name='취미'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
    ]
