# Generated by Django 4.2.7 on 2024-01-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_fooditems_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditems',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
