# Generated by Django 3.1.7 on 2021-08-25 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0051_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpro',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='orderpro',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='orderpro',
            name='item',
        ),
        migrations.AddField(
            model_name='size',
            name='size_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datawork.category'),
        ),
        migrations.DeleteModel(
            name='Ordering',
        ),
        migrations.DeleteModel(
            name='OrderPro',
        ),
    ]
