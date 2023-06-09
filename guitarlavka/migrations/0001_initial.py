# Generated by Django 4.1.7 on 2023-06-19 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Гітара', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='URL')),
                ('brand', models.CharField(max_length=100, verbose_name='Виробник')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('description', models.TextField(verbose_name='Опис')),
                ('string_number', models.IntegerField(default=6, verbose_name='Кількість струн')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кількість товару')),
                ('picture', models.ImageField(blank=True, default='product_images/1.png', null=True, upload_to='product_images/', verbose_name='Фото')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitarlavka.categories', verbose_name='Категорія')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitarlavka.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Імя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Прізвище')),
                ('telephone', models.CharField(max_length=100, verbose_name='Номер телефону')),
                ('address', models.CharField(max_length=100, verbose_name='Адреса доставки')),
                ('comment', models.TextField(blank=True, max_length=100, null=True, verbose_name='Коментарій до замовлення')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_items', models.ManyToManyField(to='guitarlavka.orderitem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='guitarlavka.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitarlavka.product')),
            ],
        ),
    ]
