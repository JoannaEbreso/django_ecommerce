from django.urls import path

from . import views

app_name = 'electronics'
urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('add_product_to_cart/', views.add_product_to_cart, name="add_product_to_cart"),
    path('all_cart/', views.display_no_cart_items, name="display_no_cart_items"),
    path('update_quantity/', views.update_cart_quantity, name="update_quantity"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.auth_login, name="login"),
    path('logout/', views.auth_logout, name="logout"),
    path('compAccess/', views.computer_accessories, name="comp_access"),

]