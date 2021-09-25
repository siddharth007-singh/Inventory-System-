# Generated by Django 3.1.7 on 2021-08-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0021_auto_20210731_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='issue',
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_status',
            field=models.CharField(choices=[('0', 'PAY'), ('1', 'CREDIT')], max_length=100, null=True),
        ),
    ]