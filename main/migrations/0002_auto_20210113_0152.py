# Generated by Django 3.0.7 on 2021-01-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='City',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='register',
            name='Comment',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
