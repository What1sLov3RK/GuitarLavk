from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import Product, Cart, CartItem, Order
from .forms import CategoryFilterForm, RegisterForm, OrderForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import transaction
from django.views.generic import ListView, View, CreateView
from django.contrib.auth.forms import AuthenticationForm
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_control


class Home(DataMixin, View):
    model = Product
    template_name = 'index.html'
    context_object_name = 'product', 'cart_quantity',

    def get_queryset(self):
        return self.model.objects.all()[:5]

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        cart = self.cart(request)
        cart_quantity = self.cart_quantity(cart)
        context = {
            self.context_object_name[0]: products,
            'cart_quantity': cart_quantity,
        }

        return render(request, self.template_name, context)


class Catalogue(DataMixin, View):
    form_class = CategoryFilterForm
    model = Product
    template_name = 'catalogue.html'
    success_url = '/catalogue/'

    def get_queryset(self):
        return self.model.objects.all()

    def form_valid(self, form):
        categories = form.cleaned_data['categories']
        return categories

    def form_invalid(self, form):
        return messages.error("Invalid form")

    def get(self, request, *args, **kwargs):
        cart = self.cart(request)
        cart_quantity = self.cart_quantity(cart)
        products = self.model.objects.all()
        form = self.form_class(request.GET or None)
        if request.GET and form.is_valid():
            categories = self.form_valid(form)
            products = products.filter(type__in=categories)
        quantity_of_diff_products = products.count()
        context = {
            'products': products,
            'category_filter_form': form,
            'cart_quantity': cart_quantity,
            'count': quantity_of_diff_products
        }
        return render(request, self.template_name, context)


class Product_view(DataMixin, View):
    template_name = 'product.html'
    model = Product
    context_object_name = 'product', 'cart_quantity'

    def get(self, request, product_slug, *args, **kwargs):
        cart = self.cart(request)
        cart_quantity = self.cart_quantity(cart)
        product = get_object_or_404(self.model, slug=product_slug)
        context = {
            self.context_object_name[0] : product,
            self.context_object_name[1]: cart_quantity,
        }
        return render(request, self.template_name, context)


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if int(cart_item.get_item_quantity()) > 1:
        cart_item.set_item_quantity(cart_item.get_item_quantity() - 1)
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


class AddToCart(DataMixin, View):
    model = CartItem
    success_url = 'cart/'

    def get(self, request, product_slug):
        cart = self.cart(request)
        product = get_object_or_404(Product, slug=product_slug)
        if product.quantity > 0:
            cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not item_created:
                if product.get_product_quantity() > cart_item.get_item_quantity():
                    cart_item.quantity += 1
                    cart_item.save()
            cart_item.order = None
            cart_item.save()
            return redirect('cart')


class Cart_view(DataMixin, View):
    model = Order
    context_object_name = 'cart_items'
    form_class = OrderForm

    def form_valid(self, request, form):
        cart = self.cart(request)
        cart_items = cart.get_cart_items()
        if cart_items.count() > 0:
            first_name = form.cleaned_data ['first_name']
            last_name = form.cleaned_data ['last_name']
            telephone = form.cleaned_data ['telephone']
            address = form.cleaned_data ['address']
            comment = form.cleaned_data ['comment']
            with transaction.atomic():
                order = self.model.objects.create(address=address, comment=comment,
                                                      price=cart.get_total_price(), telephone=telephone,
                                                      first_name=first_name, last_name=last_name)
                if not request.user.is_anonymous:
                    order.user = request.user
                    order.save()
                order.products.set(cart_items.values_list('product', flat=True))
                for cart_item in cart_items:
                    product = cart_item.product
                    product.quantity -= cart_item.quantity
                    product.save()
                cart.delete()
                return order_success(request, order)
        else:
            return redirect('catalogue')

    def form_invalid(self, form):
        return redirect('home')

    def get(self, request, *args, **kwargs):
        cart = self.cart(request)
        cart_quantity = self.cart_quantity(cart)
        cart_items = cart.get_cart_items()
        total_price = cart.get_total_price()
        form = self.form_class(request.GET)
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'cart_quantity': cart_quantity,
            'order_form': form
        }
        return render(request, 'cart.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def logout_view(request):
    logout(request)
    return redirect('home')


def order_success(request, order):
    return render(request, 'order_success.html', {'order_id': order.id})
