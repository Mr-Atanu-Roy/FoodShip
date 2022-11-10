# Generated by Django 4.1.3 on 2022-11-10 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address_email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='buyer_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_mode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]