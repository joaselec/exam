# Generated by Django 2.2.2 on 2019-09-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20190904_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='hits',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]