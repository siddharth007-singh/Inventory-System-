# Generated by Django 3.1.7 on 2021-08-25 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0052_auto_20210825_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('qty', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='datawork.category')),
            ],
        ),
    ]
