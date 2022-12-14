# Generated by Django 4.1.2 on 2022-11-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered'), ('canceled', 'canceled')], default='canceled', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(default='not done', max_length=255),
        ),
    ]
