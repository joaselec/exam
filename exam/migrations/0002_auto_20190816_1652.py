# Generated by Django 2.2.2 on 2019-08-16 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solvec',
            old_name='check_YN',
            new_name='check',
        ),
    ]
