import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Item, ItemOrder, Order


def add_to_order(request, id, slug):
    item = get_object_or_404(Item, id=id)
    order, created = Order.objects.get_or_create(
        session_key=request.session.session_key
    )
    order_item, item_created = ItemOrder.objects.get_or_create(
        order=order, item=item
    )
    if not item_created:
        order_item.quantity += 1
        order_item.save()
    return redirect(f'products:{slug}')


def order_view(request):
    return render(
        request, 'products/order.html',
        {
            'items_order': ItemOrder.objects.filter(
                order__session_key=request.session.session_key
            )
        }
    )


def clear_order(request):
    Order.objects.filter(session_key=request.session.session_key).delete()
    return redirect('products:product-list')


class ProductList(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'products/product_list.html'


class ProductDetail(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'products/product_detail.html'


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCheckoutSessionView(DetailView):
    def get(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item.item.price * 100),
                        'product_data': {
                            'name': item.item.name,
                            'description': item.item.description,
                        },
                    },
                    'quantity': item.quantity,
                } for item in ItemOrder.objects.filter(order=self.kwargs['pk'])
            ],
            mode='payment',
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = 'products/success.html'


class CancelView(TemplateView):
    template_name = 'products/cancel.html'
