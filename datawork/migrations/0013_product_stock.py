# Generated by Django 3.1.7 on 2021-07-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0012_issue_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('0', 'show'), ('1', 'hide')], default='0', max_length=100, null=True),
        ),
    ]