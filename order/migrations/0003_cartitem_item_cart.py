# Generated by Django 4.2.7 on 2024-01-17 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='Item_cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='order.cart'),
        ),
    ]
