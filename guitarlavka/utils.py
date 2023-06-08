from django.utils.decorators import method_decorator
from .models import Cart
from GuitarLavk import settings


class DataMixin:
    def cart(self, request):
        session = request.session.get(settings.CART_SESSION_ID)
        cart, created = Cart.objects.get_or_create(session=session)
        return cart

    def cart_quantity(self, cart):
        cart_quantity = cart.get_cart_item_number()
        return cart_quantity

