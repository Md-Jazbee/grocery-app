# Generated by Django 3.2.5 on 2021-07-24 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=128)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
