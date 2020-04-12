"""
-- coding: utf-8 --
@Time : 2020/4/13 2:22
@Author : jcoool
@Site : 
@File : urls.py
@Software: PyCharm
"""
from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]