# Generated by Django 5.1 on 2024-09-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
