# Generated by Django 3.0.2 on 2020-01-14 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inboxApp', '0007_auto_20200113_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inboxdb',
            options={'verbose_name_plural': 'User Inboxes'},
        ),
        migrations.RemoveField(
            model_name='inboxdb',
            name='conversation',
        ),
        migrations.AddField(
            model_name='inboxdb',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inboxdb',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserConversation',
        ),
    ]
