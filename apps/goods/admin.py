from django.contrib import admin
from goods import models


class GoodsAdmin(admin.ModelAdmin):
    # 显示的字段，字段可以在model处理，如：加html标签（添加着色，加粗...）
    list_display = ['name', 'colored_desc', 'date', 'price']
    # 排序,可以使用多个字段进行排序
    ordering = ['name', 'date', 'price']
    # 过虑字段
    list_filter = ['name', 'date']
    # 日期字段特殊处理，...
    date_hierarchy = 'date'
    # 搜索字段
    search_fields = ('name', )
    # 多对多字段编辑美化处理
    filter_horizontal = ('shop',)
    # 分布，每页显示的数据量
    list_per_page = 2
    # 通过 date 可以点击进入编辑
    list_display_links = ['date']
    # 在展示页面进行编辑
    list_editable = ('name',)
    fieldsets = [
        ('基本信息', {'fields': ['name', 'desc']}),
        ('商家', {'fields': ['shop']})
    ]


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'num']
    ordering = ['-num']


admin.site.register(models.Goods, GoodsAdmin)
admin.site.register(models.Shop, ShopAdmin)
admin.site.register(models.Price, PriceAdmin)

admin.site.site_header = '积分平台'
admin.site.site_title = '瑞银'
