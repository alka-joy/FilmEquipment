# Generated by Django 5.0 on 2023-12-30 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_complainttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rentcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
    ]