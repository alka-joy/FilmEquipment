# Generated by Django 5.0 on 2024-03-03 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0011_tbl_sellerfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_productgallery',
            name='rentitem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Seller.tbl_rentitem'),
        ),
    ]
