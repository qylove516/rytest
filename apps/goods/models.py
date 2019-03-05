from django.db import models


# Create your models here.

class Goods(models.Model):
    name = models.CharField('名称', max_length=64, blank=True, null=True)
    desc = models.TextField('描述', blank=True, null=True)
    date = models.DateField('日期', auto_now_add=True)
    shop = models.ManyToManyField(
        'Shop',
        verbose_name='商家',
        related_name='goods_shop_item'
    )
    price = models.ForeignKey(
        'Price',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='价格',
        related_name='goods_price_item'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'


class Shop(models.Model):
    name = models.CharField('名称', max_length=64, blank=True, null=True)
    address = models.CharField('地址', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商家'
        verbose_name_plural = '商家'


class Price(models.Model):
    name = models.CharField('名称', max_length=64, blank=True, null=True)
    num = models.IntegerField('价格', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '价格'
        verbose_name_plural = '价格'


class Order(models.Model):
    name = models.CharField('名称', max_length=64, blank=True, null=True)
    num = models.IntegerField('数量', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'
