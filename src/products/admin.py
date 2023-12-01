from django.contrib import admin

from .models import Item, ItemOrder, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


class ItemOrderAdmin(admin.StackedInline):
    model = ItemOrder


@admin.register(Order)
class OrederAdmin(admin.ModelAdmin):
    inlines = (ItemOrderAdmin,)

    class Meta:
        model = Order
