# Generated by Django 5.0 on 2024-01-26 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_newseller'),
        ('Seller', '0002_tbl_rentitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_rentitem',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_newseller'),
        ),
    ]
