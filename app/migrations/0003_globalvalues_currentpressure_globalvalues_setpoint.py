# Generated by Django 5.0 on 2024-01-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_globalvalues'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalvalues',
            name='currentPressure',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='globalvalues',
            name='setPoint',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6),
        ),
    ]
