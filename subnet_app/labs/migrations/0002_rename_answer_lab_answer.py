# Generated by Django 3.2.5 on 2021-07-30 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='answer',
            new_name='lab_answer',
        ),
    ]
