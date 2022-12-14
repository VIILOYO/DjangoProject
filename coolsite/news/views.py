from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin, UpdateView
from django.shortcuts import render, redirect

from .models import Comment, News
from . forms import CategoryForm, CommentForm, NewsForm
from registration.models import User
from registration.forms import CreateUserForm


class NewsList(ListView):
    """Отображение новостей"""

    model = News
    paginate_by = 5
    template_name = 'news/HomePage.html'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """Фильтр записей"""
        return News.objects.filter(is_published=True)


class NewsDetail(FormMixin, DetailView):
    """Отображение новости полностью"""
    model = News
    template_name = 'news/NewsDetail.html'
    slug_url_kwarg = 'news_slug'
    form_class = CommentForm

    def post(self, request, *args, **kwarg):
        """Функция публикации"""
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """Валидация формы"""
        self.object = form.save()
        self.object.news = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        """Успешная переадресация"""
        return reverse_lazy('NewsDetail', kwargs={'news_slug': self.get_object().slug})

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = context['object']
        return context

    def get_object(self, queryset=None):
        """Счетчик просмотров"""
        obj = super(NewsDetail, self).get_object(queryset=queryset)
        obj.views +=1
        obj.save()
        return obj


class CategoryList(ListView):
    """Отображение новостей по категориям"""

    model = News
    paginate_by = 5
    template_name = 'news/HomePage.html'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """Фильтр записей"""
        return News.objects.filter(is_published=True, categories__slug=self.kwargs['category_slug'])


class CreateNews(PermissionRequiredMixin, CreateView):
    """Обработка формы новости"""
    permission_required = ('registration.view_User', )
    login_url = 'HomePage'
    form_class = NewsForm
    template_name = 'news/AddNews.html'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление новости'
        return context


class CreateCategory(PermissionRequiredMixin, CreateView):
    """Обработка формы категории"""
    permission_required = ('registration.view_User', )
    login_url = 'HomePage'
    form_class = CategoryForm
    template_name = 'news/AddNews.html'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление категории'
        return context


class ProfileUpdate(UpdateView):
    """Обновление данных профиля"""
    model = User
    form = CreateUserForm
    template_name = 'news/UpdateProfile.html'
    pk_url_kwarg = 'user_id'
    fields = ['first_name', 'last_name', 'email']

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context

    def get_success_url(self, **kwargs):
        """Успешная переадресация"""
        return reverse_lazy('profile')


@user_passes_test(lambda u: u.is_superuser)
def delete_comment(request, comment_id):
    """Удаление комментария"""
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('NewsDetail', news_slug=comment.news.slug)


def contacts(request):
    """Контакты .../contacts"""
    return render(request, 'news/contacts.html',
                  context={'title': 'Контакты'})


def profile(request):
    """Профиль, смысла в нем пока нет"""
    if request.user.is_authenticated:
        return render(request, 'news/profile.html', {'title': 'Профиль'})
    else:
        return redirect('HomePage')
