# Generated by Django 2.2.2 on 2019-09-03 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='result',
            new_name='board',
        ),
    ]
