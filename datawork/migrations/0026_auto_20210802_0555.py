# Generated by Django 3.1.7 on 2021-08-02 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0025_auto_20210802_0448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='desc',
            new_name='cat_desc',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='name',
            new_name='cat_name',
        ),
    ]
