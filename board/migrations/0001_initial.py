# Generated by Django 2.2.2 on 2019-09-03 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('detail', models.CharField(max_length=5000)),
                ('hits', models.CharField(max_length=10)),
                ('recommend', models.CharField(max_length=500)),
            ],
        ),
    ]
