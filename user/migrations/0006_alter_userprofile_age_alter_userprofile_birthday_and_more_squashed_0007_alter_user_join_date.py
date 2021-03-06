# Generated by Django 4.0.5 on 2022-06-21 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('user', '0006_alter_userprofile_age_alter_userprofile_birthday_and_more'), ('user', '0007_alter_user_join_date')]

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
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='가입일'),
        ),
    ]
