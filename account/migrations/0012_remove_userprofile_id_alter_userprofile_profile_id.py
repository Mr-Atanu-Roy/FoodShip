# Generated by Django 4.1.3 on 2022-11-10 11:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_useraddress_address_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
