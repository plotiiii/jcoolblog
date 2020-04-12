"""
-- coding: utf-8 --
@Time : 2020/4/13 2:25
@Author : jcoool
@Site : 
@File : forms.py
@Software: PyCharm
"""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']