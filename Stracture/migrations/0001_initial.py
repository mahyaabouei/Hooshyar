# Generated by Django 4.1.13 on 2024-06-23 10:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('okay', 'تعین تکلیف نشده'), ('cancel', 'لغو شده'), ('Reserv', 'رزرو')], max_length=20)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.consultant')),
            ],
        ),
    ]
