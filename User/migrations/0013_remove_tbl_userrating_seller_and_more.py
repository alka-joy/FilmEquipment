# Generated by Django 5.0 on 2024-03-03 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_tbl_servicebooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_userrating',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='tbl_userrating',
            name='serviceprovider',
        ),
        migrations.DeleteModel(
            name='tbl_servicebooking',
        ),
        migrations.DeleteModel(
            name='tbl_userrating',
        ),
    ]