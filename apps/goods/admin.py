from django.contrib import admin
from goods import models


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'date', 'price']


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'num']


admin.site.register(models.Goods, GoodsAdmin)
admin.site.register(models.Shop, ShopAdmin)
admin.site.register(models.Price, PriceAdmin)

admin.site.site_header = '积分平台'
admin.site.site_title = '瑞银'
