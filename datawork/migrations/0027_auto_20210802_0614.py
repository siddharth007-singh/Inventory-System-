# Generated by Django 3.1.7 on 2021-08-02 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0026_auto_20210802_0555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='cat_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='cat_name',
            new_name='name',
        ),
    ]
