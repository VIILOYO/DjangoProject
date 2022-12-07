from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .models import Category, News
from . forms import NewsForm


class NewsList(ListView):
    """Отображение новостей"""

    model = News
    paginate_by = 10
    template_name = 'news/HomePage.html'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """Фильтр записей"""
        return News.objects.filter(is_published=True)


class NewsDetail(DetailView):
    """Отображение новости полностью"""
    model = News
    template_name = 'news/NewsDetail.html'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = context['object']
        return context


class CategoryDetail(DetailView):
    """Отображение новостей по категориям"""
    model = Category
    template_name = 'news/CategoryDetail.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = context['object']
        return context


class CreateNews(CreateView):
    """Обработка формы новости"""
    form_class = NewsForm
    template_name = 'news/AddNews.html'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление новости'
        return context


def contacts(request):
    """Контакты .../contacts"""
    return render(request, 'news/contacts.html',
                  context={'title': 'Контакты'})