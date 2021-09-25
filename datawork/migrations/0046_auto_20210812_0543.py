# Generated by Django 3.1.7 on 2021-08-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0045_order_pay_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_method',
            field=models.CharField(choices=[('0', 'credit'), ('1', 'cash')], max_length=100, null=True),
        ),
    ]
