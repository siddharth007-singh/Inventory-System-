# Generated by Django 3.1.7 on 2021-08-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0034_remove_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
