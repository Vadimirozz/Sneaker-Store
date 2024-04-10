from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        # Получаем или создаем корзину в сессии
        cart = request.session.get('cart', {})
        
        # Обновляем количество товара в корзине
        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] = {'product': product, 'quantity': quantity}
        
        # Сохраняем корзину в сессии
        request.session['cart'] = cart

        return JsonResponse({'success': True, 'quantity': quantity})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def view_cart(request):
    cart_items = []
    total_price = 0
    
    # Проверяем, есть ли уже корзина в сессии
    if 'cart' in request.session:
        cart = request.session['cart']
        # Получаем объекты товаров из базы данных на основе данных о корзине в сессии
        for item_data in cart.values():
            product = item_data['product']
            size = item_data['size']
            quantity = item_data['quantity']
            total_price += product.price * quantity
            cart_items.append({'product': product, 'size': size, 'quantity': quantity})
    
    return render(request, 'main/cart.html', {'cart_items': cart_items, 'total_price': total_price})

