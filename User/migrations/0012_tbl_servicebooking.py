# Generated by Django 5.0 on 2024-03-02 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_tbl_adminlogin'),
        ('ServiceProvider', '0005_initial'),
        ('User', '0011_delete_tbl_servicebooking'),
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