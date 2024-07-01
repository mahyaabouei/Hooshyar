# Generated by Django 4.1.13 on 2024-07-01 09:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='KindOfCounseling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('price', models.IntegerField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='Hooshyar/Static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.IntegerField()),
                ('question_2', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
                ('question_4', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
                ('question_5', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
                ('question_6', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
                ('question_7', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
                ('question_8', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
                ('question_9', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
                ('question_10', models.IntegerField(choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'j'), (10, 'k')])),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cost', models.IntegerField()),
                ('survey', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('note', django_summernote.fields.SummernoteTextField()),
                ('status', models.CharField(choices=[('completing', 'completing'), ('waiting', 'waiting'), ('done', 'done'), ('cancel', 'cancel')], max_length=20)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.consultant')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.auth')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visit.kindofcounseling')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visit.question')),
            ],
        ),
    ]
