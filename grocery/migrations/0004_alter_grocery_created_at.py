# Generated by Django 3.2.5 on 2021-07-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0003_auto_20210724_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
