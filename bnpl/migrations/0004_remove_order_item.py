# Generated by Django 5.1 on 2024-09-03 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bnpl', '0003_user_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
    ]
