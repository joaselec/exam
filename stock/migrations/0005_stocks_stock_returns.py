# Generated by Django 2.2.2 on 2019-12-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20191206_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='stock_returns',
            field=models.CharField(max_length=255, null=True),
        ),
    ]