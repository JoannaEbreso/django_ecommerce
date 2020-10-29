from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views import generic

from . import forms
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category, Cart


def index(request):
    products = Product.objects.all()
    session_id = request.session.session_key
    print(type(session_id))
    print(session_id)
    items_in_cart = Cart.objects.all()
    num_of_items = len(items_in_cart)
    print(num_of_items)
    for p in products:
        print(p)
    return render(request, 'index.html', {'products': products, 'session_id': session_id, 'num_of_items': num_of_items})


def cart(request):
    if request.user.is_authenticated:
        items_in_cart = Cart.objects.all()
        num_of_item = len(items_in_cart)
        total_price_of_product = 0.0
        for cart_items in items_in_cart:
            total_price_of_product = total_price_of_product + cart_items.product.product_price

        return render(request, 'cart.html',
                      {'items_in_cart': items_in_cart, 'num_of_item': num_of_item,
                       'total_price_of_product': total_price_of_product})

    else:
        return redirect('electronics:login')


def checkout(request):
    items_in_cart = Cart.objects.all()
    num_of_item = len(items_in_cart)
    total_price_of_product = 0.0
    for cart_items in items_in_cart:
        total_price_of_product = total_price_of_product + cart_items.product.product_price
        print(cart_items.quantity)

    return render(request, 'checkout.html',
                  {'items_in_cart': items_in_cart, 'num_of_item': num_of_item,
                   'total_price_of_product': total_price_of_product})


def signup(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print(user)
            messages.success(request, f'Registration complete! You may log in!')
            return redirect('/login')
    else:
        form = forms.SignupForm()
        for f in form:
            print("form value {}".format(f.errors))
    return render(request, 'signup.html', {'form': form})


def auth_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        # print(form.errors)
        print(form)
        print(form.cleaned_data)
        print(f'form is valid {form.is_valid()} and the function definition {form.is_valid}')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            print(f'the user is {user}')

            if user is not None:
                print(f'the user is {user}')
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("electronics:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


def auth_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("electronics:index")


def computer_accessories(request):
    products = Product.objects.all()
    comp_access_category = Category.objects.filter(category_name__exact="Computer Accessories")
    session_id = request.session.session_key
    print(type(session_id))
    print(session_id)
    for c in comp_access_category:
        print(c)
    return render(request, 'compAccess.html',
                  {'comp_access_category': c, 'session_id': session_id, 'products': products})


def display_no_cart_items(request):
    items_in_cart = Cart.objects.all()
    num_of_items = len(items_in_cart)
    print(num_of_items)
    return HttpResponse(num_of_items)


def add_product_to_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        product = get_object_or_404(Product, pk=product_id)
        try:
            Cart.objects.get(product=product)
        except ObjectDoesNotExist:
            new_cart_item = Cart(product=product, quantity=1)
            new_cart_item.save()

        items_in_cart = Cart.objects.all()
        num_of_items = len(items_in_cart)
        return HttpResponse(num_of_items)  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


def update_cart_quantity(request):
    print(request)
    if request.method == 'GET':
        cart_id = request.GET['cart_id']
        quantity = request.GET['product_quantity']
        cart = get_object_or_404(Cart, pk=cart_id)
        print(cart)
        if cart is not None:
            cart.quantity = quantity
            cart.save()
        return HttpResponse(cart)  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")
