# Generated by Django 5.0 on 2024-03-03 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_tbl_adminlogin'),
        ('ServiceProvider', '0006_delete_tbl_services'),
        ('User', '0013_remove_tbl_userrating_seller_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_serviceprovider',
        ),
    ]
