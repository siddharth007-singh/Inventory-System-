# Generated by Django 3.1.7 on 2021-07-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0016_auto_20210731_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='issue',
        ),
        migrations.AddField(
            model_name='issue',
            name='issue',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
