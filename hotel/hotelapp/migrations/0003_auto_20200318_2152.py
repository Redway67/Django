# Generated by Django 3.0.3 on 2020-03-18 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotelapp', '0002_bookingorder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]