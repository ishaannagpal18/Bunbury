# Generated by Django 3.1 on 2022-10-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='auth_token',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
