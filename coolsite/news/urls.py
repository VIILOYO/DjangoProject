from django.urls import path

from .views import CreateCategory, CategoryList, delete_comment, ProfileUpdate, CreateNews, NewsDetail, NewsList, contacts, profile


urlpatterns = [
    path('', NewsList.as_view(), name='HomePage'),
    path('profile', profile, name='profile'),
    path('contacts', contacts, name='contacts'),
    path('news/<slug:news_slug>/', NewsDetail.as_view(), name='NewsDetail'),
    path('category/<slug:category_slug>/', CategoryList.as_view(), name='CategoryDetail'),
    path('comment_delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('add_category', CreateCategory.as_view(), name='AddCategory'),
    path('add_news', CreateNews.as_view(), name='AddNews'),
    path('update_profile/<int:user_id>/', ProfileUpdate.as_view(), name='ProfileUpdate')
]
