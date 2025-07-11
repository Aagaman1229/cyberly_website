# urls.py inside the `main` app
from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('', article_list, name='article-list'),
    path('<slug:slug>/', article_detail, name='article-detail'),
]
