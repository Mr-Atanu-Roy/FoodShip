# Generated by Django 4.1.2 on 2022-11-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurant_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='closes_at',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='opens_at',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='timing',
            field=models.CharField(default='10 AM to 12 Midnight', max_length=255),
        ),
    ]
