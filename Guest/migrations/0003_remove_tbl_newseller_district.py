# Generated by Django 5.0 on 2023-12-30 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_tbl_newseller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_newseller',
            name='district',
        ),
    ]
