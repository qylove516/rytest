import jieba
from django import template


register = template.Library()


@register.filter
def test():
    print(123)
    return 123
