# Generated by Django 5.0.6 on 2024-06-02 08:46

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('interactions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Company_name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=128)),
                ('ratings', models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]
