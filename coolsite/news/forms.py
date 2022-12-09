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
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'