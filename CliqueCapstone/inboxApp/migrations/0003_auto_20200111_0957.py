# Generated by Django 3.0.2 on 2020-01-11 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inboxApp', '0002_auto_20200111_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directmsgdb',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='inboxdb',
            name='messages',
        ),
        migrations.AddField(
            model_name='directmsgdb',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='directmsgdb',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
