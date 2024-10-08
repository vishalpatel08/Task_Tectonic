# Generated by Django 5.1 on 2024-09-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpl', '0004_remove_order_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=15)),
                ('userid', models.CharField(max_length=10)),
                ('itemid', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=122)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
