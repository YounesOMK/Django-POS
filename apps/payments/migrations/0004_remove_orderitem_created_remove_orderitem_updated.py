# Generated by Django 4.1 on 2022-08-25 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0003_remove_order_paid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitem",
            name="created",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="updated",
        ),
    ]
