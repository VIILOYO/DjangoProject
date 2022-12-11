from django import template
from datetime import datetime as dt

from news.models import Category, News


register = template.Library()

@register.simple_tag()
def get_categories():
    """Получение списка категорий"""
    return Category.objects.all()

@register.simple_tag()
def get_news():
    """Получение 5 самых популярных новостей за неделю"""
    today = dt.today()
    return News.objects.filter(date_publication__day__lte=today.day).filter(date_publication__day__gte=today.day-5).order_by('-views')[:5]
