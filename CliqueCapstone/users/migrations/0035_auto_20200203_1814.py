# Generated by Django 3.0.2 on 2020-02-04 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_remove_userprofile_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends_list',
        ),
        migrations.CreateModel(
            name='UserFriendsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends_list', models.ManyToManyField(related_name='friends_list', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users_friend_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'FriendsList',
            },
        ),
    ]
