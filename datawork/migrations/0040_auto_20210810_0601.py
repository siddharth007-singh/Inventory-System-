# Generated by Django 3.1.7 on 2021-08-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0039_remove_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
