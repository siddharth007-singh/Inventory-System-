# Generated by Django 3.1.7 on 2021-08-24 15:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0050_orderpro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('pay_method', models.CharField(choices=[('Credit', 'Credit'), ('Paid', 'Paid')], max_length=100, null=True)),
                ('discount_price', models.CharField(blank=True, max_length=150, null=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('c_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datawork.customer')),
                ('items', models.ManyToManyField(to='datawork.OrderPro')),
            ],
        ),
    ]
