from django import template
from django.core.paginator import Paginator
from django.http import request

from flower.models import *

register = template.Library()

@register.simple_tag(name='categories')
def get_categories(filter=None, cat_selected=0):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.all().order_by(filter)

@register.simple_tag
def get_paginator(categ_slug=None, page_number=None):
    if not categ_slug:
        flo = Flower.objects.all().select_related('cat')
        paginator = Paginator(flo, 3)
        page_obj = paginator.get_page(page_number)
        return page_obj
    else:
        flo = Flower.objects.filter(cat__slug=categ_slug).select_related('cat')
        paginator = Paginator(flo, 3)
        page_obj = paginator.get_page(page_number)
        return page_obj
# @register.inclusion_tag('flower/tag.html')
# def get_category(sort=None):
#     if sort==None:
#         cats = Category.objects.all()
#     else:
#         cats = Category.objects.all().order_by(sort)
#     return {'cats':cats}