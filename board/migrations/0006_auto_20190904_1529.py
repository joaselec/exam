# Generated by Django 2.2.2 on 2019-09-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20190904_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='hits',
            field=models.IntegerField(default=1, max_length=10),
        ),
    ]
