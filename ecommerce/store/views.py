# store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    # Get the product or return a 404 if not found
    product = get_object_or_404(Product, id=product_id)
    
    # Get the cart from session, or initialize it
    cart = request.session.get('cart', {})

    # Increase the quantity if product already in cart, otherwise set to 1
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    # Save the cart back into the session
    request.session['cart'] = cart
    return redirect('product_list')

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    # Build a list of cart items with product details
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity,
        })
    
    # Calculate grand total
    grand_total = sum(item['total_price'] for item in cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'grand_total': grand_total})
