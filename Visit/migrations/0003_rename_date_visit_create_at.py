# Generated by Django 4.1.13 on 2024-07-01 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Visit', '0002_question_question_3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='date',
            new_name='create_at',
        ),
    ]
