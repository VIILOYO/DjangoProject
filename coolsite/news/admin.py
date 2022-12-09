from django.contrib import admin

from .models import Category, Comment, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug',
                    'date_publication', 'date_update',
                    'get_categories', 'views',
                    'is_published',]
    list_display_links = ['id', 'title', 'slug']
    list_editable = ['is_published']
    search_fields = ['title', 'content']
    list_filter = ['categories', 'is_published']
    filter_vertical = ['categories']
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['views', 'comments']

admin.site.register(News, NewsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'text', 'news']
    list_display_links = ['id', 'text']
    search_fields = ['author', 'text', 'news']
    list_filter = ['author', 'news']

admin.site.register(Comment, CommentAdmin)