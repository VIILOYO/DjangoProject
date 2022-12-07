from django.db import models
from django.urls import reverse

from registration.models import User


class Comment(models.Model):
    """Комментарии"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(max_length=1000, verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text


class Category(models.Model):
    """Категории новостей"""
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class News (models.Model):
    """Модель новости"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='Текст новости')
    image = models.ImageField(upload_to='media/%Y/%m/%d/', verbose_name='Изображение')
    date_publication = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_categories(self):
        """Преобразование списка категорий в строку"""
        return ", ".join([category.name for category
                          in self.categories.all()])

    def get_absolute_url(self):
        """Возврат самой новости"""
        return reverse('NewsDetail', kwargs={'news_slug': self.slug})
