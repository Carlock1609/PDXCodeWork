# Generated by Django 3.0.2 on 2020-01-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200114_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='follower_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo_library',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_media',
            field=models.URLField(blank=True, null=True),
        ),
    ]