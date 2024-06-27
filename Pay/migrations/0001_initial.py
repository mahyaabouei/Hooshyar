# Generated by Django 4.1.13 on 2024-06-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('kind', models.CharField(choices=[('per', 'per'), ('val', 'val')], max_length=10)),
                ('expiration_date', models.DateTimeField()),
                ('number_of_times', models.IntegerField()),
            ],
        ),
    ]
