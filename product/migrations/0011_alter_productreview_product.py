# Generated by Django 4.1.3 on 2022-11-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_productreview_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
