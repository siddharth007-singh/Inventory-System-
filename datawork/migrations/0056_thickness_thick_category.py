# Generated by Django 3.1.7 on 2021-09-07 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0055_brand_brand_cxategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='thickness',
            name='thick_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datawork.category'),
        ),
    ]
