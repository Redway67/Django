# Generated by Django 3.0.3 on 2020-04-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0003_auto_20200322_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
