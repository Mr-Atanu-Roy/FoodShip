# Generated by Django 4.1.2 on 2022-11-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_order_status_alter_order_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
