from django.forms import ModelForm

from .models import News


class NewsForm(ModelForm):
    """Форма создания новости"""
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'categories', 'image']
