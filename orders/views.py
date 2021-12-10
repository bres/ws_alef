from django.shortcuts import render, redirect
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm
import datetime
from .models import Order, Payment
import json


def payments(request):
    body = json.loads(request.body)
    print(body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])


    # Store transaction details inside Payment model
    payment = Payment(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=order.order_total,
        status=body['status'],
    )
    payment.save()

    order.payment = payment
    order.is_ordered = True
    order.save()

    return render(request, 'orders/payments.html', )


def place_order(request, total=0, quantity=0):
    current_user = request.user
    # id the cart count is less or equal then reidrect to store list of items
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store:product_list')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    # tax =0 (2 * total)/100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside Order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.municipality = form.cleaned_data['municipality']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.post_code = form.cleaned_data['post_code']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.tax = tax
            data.order_total = grand_total
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")  # 20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,  # optional
                'grand_total': grand_total,
            }
            return render(request, 'orders/payments.html', context)

    else:
        return redirect('carts:checkout')
