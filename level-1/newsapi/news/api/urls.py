from django.urls import path
# from news.api.views import (article_list_create_api_view,
#                                                   article_detail_api_view)

from news.api.views import ArticleDetailedAPIView,ArticleListCreateAPIView,JournalistCreateAPIView
    
    
urlpatterns=[
    path('articles/',
         ArticleListCreateAPIView.as_view(),
         name='article-list'),
    path('articles/<int:pk>',
         ArticleDetailedAPIView.as_view(),
         name='article-detail'),
    path('journalists/',
         JournalistCreateAPIView.as_view(),
         name='journalist-list'),
    
]