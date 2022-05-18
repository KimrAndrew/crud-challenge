# Generated by Django 4.0.2 on 2022-05-18 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0005_inventoryitem_delete_customer_and_more'),
        ('warehouse_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseInventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_inventory', models.PositiveIntegerField(default=0)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.inventoryitem')),
                ('warehouse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='warehouse_manager.warehouse')),
            ],
        ),
    ]