# Generated by Django 3.1.7 on 2021-07-28 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0007_auto_20210728_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='size_doc',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
