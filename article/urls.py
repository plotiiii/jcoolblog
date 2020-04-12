"""
-- coding: utf-8 --
@Time : 2020/4/11 21:48
@Author : jcoool
@Site : 
@File : urls.py
@Software: PyCharm
"""
from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]
