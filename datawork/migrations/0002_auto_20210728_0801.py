# Generated by Django 3.1.7 on 2021-07-28 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='doc',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]