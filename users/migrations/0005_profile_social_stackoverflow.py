# Generated by Django 4.0.4 on 2022-05-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
