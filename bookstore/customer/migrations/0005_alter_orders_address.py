# Generated by Django 4.0.2 on 2022-02-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_orders_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=120),
        ),
    ]