# Generated by Django 3.0.2 on 2020-01-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20200130_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolibrary',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
