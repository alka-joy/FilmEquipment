# Generated by Django 5.0 on 2024-03-02 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0003_initial'),
        ('User', '0011_delete_tbl_servicebooking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_services',
        ),
    ]