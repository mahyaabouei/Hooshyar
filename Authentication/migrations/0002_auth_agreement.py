# Generated by Django 4.1.13 on 2024-07-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='agreement',
            field=models.BooleanField(default=False),
        ),
    ]
