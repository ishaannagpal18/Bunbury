# Generated by Django 3.1 on 2022-10-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0003_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]