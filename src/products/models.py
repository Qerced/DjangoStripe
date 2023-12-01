from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F, Sum


class Item(models.Model):
    name = models.CharField(verbose_name='Имя товара', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=255)
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00, 'Значение должно быть больше 0.')
        ]
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        through='ItemOrder',
        related_name='order'
    )
    session_key = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def total_price(self):
        return self.itemorder_set.aggregate(
            total_price=Sum(F('quantity') * F('item__price'))
        )['total_price']


class ItemOrder(models.Model):
    order = models.ForeignKey(
        Order, verbose_name='Заказ', on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item, verbose_name='Товар', on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество товара', default=1
    )
