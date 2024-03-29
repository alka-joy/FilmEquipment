# Generated by Django 5.0 on 2023-12-30 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_rentcategory'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('photo', models.FileField(upload_to='Userdocs/')),
                ('proof', models.FileField(upload_to='Userdocs/')),
                ('password', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
