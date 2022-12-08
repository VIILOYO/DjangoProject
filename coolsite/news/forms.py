from django.forms import ModelForm

from .models import Comment, News


class NewsForm(ModelForm):
    """Форма создания новости"""
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'categories', 'image']


class CommentForm(ModelForm):
    """Форма создания комментария"""
    class Meta:
        model = Comment
        fields = ['author', 'email', 'text']