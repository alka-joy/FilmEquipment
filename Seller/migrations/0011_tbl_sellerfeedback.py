# Generated by Django 5.0 on 2024-03-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0010_tbl_sellercomplaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_sellerfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=50)),
                ('feedbackdate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]