# Generated by Django 3.1.7 on 2021-07-31 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0020_auto_20210731_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='issue_discount',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='issue_qty',
        ),
    ]