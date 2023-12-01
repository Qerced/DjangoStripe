from django.urls import path

from .views import (CancelView, CreateStripeCheckoutSessionView, ProductDetail,
                    ProductList, SuccessView, add_to_order, clear_order,
                    order_view)

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('order/', order_view, name='order-view'),
    path('add_order/<int:id>/<slug:slug>/', add_to_order, name='add-order'),
    path('clear_order/', clear_order, name='clear-order'),
    path('item/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path(
        'buy/<int:pk>/',
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
