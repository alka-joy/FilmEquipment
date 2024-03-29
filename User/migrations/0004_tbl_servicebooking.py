# Generated by Django 5.0 on 2024-02-18 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_tbl_serviceprovider'),
        ('ServiceProvider', '0003_initial'),
        ('User', '0003_alter_tbl_cart_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_servicebooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booked_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceProvider.tbl_services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newuser')),
            ],
        ),
    ]
