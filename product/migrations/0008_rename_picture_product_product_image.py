# Generated by Django 4.1.2 on 2022-10-31 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_meal_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='picture',
            new_name='product_image',
        ),
    ]
