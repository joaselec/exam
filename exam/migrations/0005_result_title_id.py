# Generated by Django 2.2.2 on 2019-08-16 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20190816_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='title_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
