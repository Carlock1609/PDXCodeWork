# Generated by Django 3.0.2 on 2020-01-13 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inboxApp', '0004_auto_20200111_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inboxdb',
            options={'verbose_name_plural': 'Inboxes'},
        ),
        migrations.CreateModel(
            name='UserConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.CharField(max_length=1000)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversation', to='inboxApp.InboxDB')),
            ],
        ),
    ]
