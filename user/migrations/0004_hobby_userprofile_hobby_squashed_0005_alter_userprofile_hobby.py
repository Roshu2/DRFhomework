# Generated by Django 4.0.5 on 2022-06-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('user', '0004_hobby_userprofile_hobby'), ('user', '0005_alter_userprofile_hobby')]

    dependencies = [
        ('user', '0003_user_is_active_user_is_admin_alter_userprofile_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hobby',
            field=models.ManyToManyField(blank=True, related_name='userprofiles', to='user.hobby'),
        ),
    ]
