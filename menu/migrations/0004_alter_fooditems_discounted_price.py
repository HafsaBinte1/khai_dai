# Generated by Django 4.2.7 on 2024-01-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_fooditems_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditems',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]