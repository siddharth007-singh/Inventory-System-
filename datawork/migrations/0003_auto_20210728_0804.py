# Generated by Django 3.1.7 on 2021-07-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0002_auto_20210728_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
