
from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('new/<int:news_id>/', GetNew.as_view(), name="new"),
    path('category/<int:category_id>/', get_category, name='category'),
    path('add_news/', CreateNews.as_view(), name='add_news'),
    path('delete/', delete, name="delete"),
    path('delete_news/<int:new_id>/', delete_new, name="delete_news"),
    path('?s=<int:title>/', search_field_title, name='title_search'),
    path('post_search/', post_search, name='search'),
    # path('auth/', CreateUser.as_view(), name='auth')
    path('get/', search, name='get_search'),
    path('login/', login)
]