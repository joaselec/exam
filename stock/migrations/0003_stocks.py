# Generated by Django 2.2.2 on 2019-12-06 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_cronlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.CharField(max_length=255)),
                ('stock_name', models.CharField(max_length=255)),
                ('start_price', models.CharField(max_length=255)),
                ('current_price', models.CharField(max_length=255)),
            ],
        ),
    ]