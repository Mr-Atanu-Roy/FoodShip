# Generated by Django 4.1.3 on 2022-11-11 02:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_picture_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('review_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('added_on', models.DateField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
