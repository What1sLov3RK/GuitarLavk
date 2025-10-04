from django.contrib import admin
from django.urls import path
from guitarlavka import views
from guitarlavka.views import (
    Home, Catalogue, Product_view,
    RegisterUser, LoginUser, Cabinet,
    OrderView, Cart_view, AddToCart,
    remove_from_cart, order_success, logout_view
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogue/product/<slug:product_slug>/', Product_view.as_view(), name='product'),
    path('', Home.as_view(), name='home'),
    path('catalogue/', Catalogue.as_view(), name='catalogue'),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name='login'),
    path("cabinet/", Cabinet.as_view(), name='cabinet'),
    path("cabinet/order/<int:order_id>", OrderView.as_view(), name='order'),
    path('cart/', Cart_view.as_view(), name='cart'),
    path('add-to-cart/<slug:product_slug>/', AddToCart.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/order_success/', order_success, name='order_success'),
    path('logout/', logout_view, name='logout'),
]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
