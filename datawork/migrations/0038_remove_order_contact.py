# Generated by Django 3.1.7 on 2021-08-10 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0037_auto_20210810_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='contact',
        ),
    ]
