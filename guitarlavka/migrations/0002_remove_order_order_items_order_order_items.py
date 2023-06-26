# Generated by Django 4.1.7 on 2023-06-19 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guitarlavka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guitarlavka.orderitem'),
            preserve_default=False,
        ),
    ]
