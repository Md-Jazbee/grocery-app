# Generated by Django 3.2.5 on 2021-07-24 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grocery', '0002_auto_20210724_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocery',
            name='modified_date',
        ),
        migrations.AddField(
            model_name='grocery',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]