# Generated by Django 3.2.5 on 2021-07-30 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lab_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_answer', models.CharField(max_length=3000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.lab_question')),
            ],
        ),
    ]
