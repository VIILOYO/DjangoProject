from django.urls import path

from .views import CategoryDetail, delete_comment, CreateNews, NewsDetail, NewsList, contacts


urlpatterns = [
    path('', NewsList.as_view(), name='HomePage'),
    path('contacts', contacts, name='contacts'),
    path('news/<slug:news_slug>/', NewsDetail.as_view(), name='NewsDetail'),
    path('category/<slug:category_slug>/', CategoryDetail.as_view(), name='CategoryDetail'),
    path('comment_delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('add_news', CreateNews.as_view(), name='AddNews'),
]
