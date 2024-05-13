# Generated by Django 4.2.10 on 2024-05-13 08:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=128)),
                ('product_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('product_price', models.FloatField()),
                ('product_rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('added_to_cart', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Products.product')),
                ('cart_quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
            ],
        ),
    ]