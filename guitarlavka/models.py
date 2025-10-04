from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.sessions.models import Session


class Categories(models.Model):
    category = models.CharField(max_length=100, default="Гітара")

    def __str__(self):
        return self.category


class Product(models.Model):
    slug = models.SlugField(primary_key=True, unique=True, db_index=True, verbose_name="URL")
    type = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Категорія")
    brand = models.CharField(max_length=100, verbose_name="Виробник")
    model = models.CharField(max_length=100, verbose_name="Модель")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    description = models.TextField(verbose_name="Опис")
    string_number = models.IntegerField(default=6, verbose_name="Кількість струн")
    quantity = models.IntegerField(default=1, verbose_name="Кількість товару")
    picture = models.ImageField(null=True, blank=True, upload_to="product_images/", default="product_images/1.png", verbose_name="Фото")

    def __str__(self):
        return str(self.type) + " " + " " + str(self.brand) + " " + str(self.model) + " " + str(self.price)


class Cart(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank=True, null=True)

    def get_cart_items(self):
        return self.cartitem_set.all()

    def get_cart_item_number(self):
        return self.cartitem_set.count()

    def get_total_price(self):
        cart_items = self.get_cart_items()
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        return total_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_item_quantity(self):
        return self.quantity

    def set_item_quantity(self, quantity):
        self.quantity = quantity

    def get_item_price(self):
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return str(self.product) + '\t\t' + str(self.quantity)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, editable=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(editable=True)

    def __str__(self) -> str:
        return str(self.product) + '\t' + str(self.quantity)


class Order(models.Model):
    id = models.AutoField(primary_key=True, editable=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_items = models.ManyToManyField(OrderItem, editable=True)
    first_name = models.CharField(max_length=100, verbose_name="Імя")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    telephone = models.CharField(max_length=100, verbose_name="Номер телефону")
    address = models.CharField(max_length=100, verbose_name="Адреса доставки")
    comment = models.TextField(max_length=100, verbose_name="Коментарій до замовлення", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.user:
            return f"Order #{self.id} by {self.user.username}"
        else:
            return f"Order #{self.id}"


