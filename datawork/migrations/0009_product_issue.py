# Generated by Django 3.1.7 on 2021-07-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0008_size_size_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='issue',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
