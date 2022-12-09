from django.forms import ModelForm

from .models import Category, Comment, News


class NewsForm(ModelForm):
    """Форма создания новости"""
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'categories', 'image']

    def __init__(self, *args, **kwargs):
        """Передача класса всем полям"""
        super(NewsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CategoryForm(ModelForm):
    """Форма создания новости"""
    class Meta:
        model = Category
        fields = ['name', 'slug']

    def __init__(self, *args, **kwargs):
        """Передача класса всем полям"""
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CommentForm(ModelForm):
    """Форма создания комментария"""
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        """Передача класса всем полям"""
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
