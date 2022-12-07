from django.urls import path

from .views import CategoryDetail, CreateNews, NewsDetail, NewsList, contacts


urlpatterns = [
    path('', NewsList.as_view(), name='HomePage'),
    path('contacts', contacts, name='contacts'),
    path('news/<slug:news_slug>', NewsDetail.as_view(), name='NewsDetail'),
    path('category/<slug:category_slug>', CategoryDetail.as_view(), name='CategoryDetail'),
    path('add_news', CreateNews.as_view(), name='AddNews'),
]
