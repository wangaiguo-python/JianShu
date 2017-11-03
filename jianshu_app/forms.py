from django.forms import ModelForm
from .models import Article
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'cover']
        help_texts = {
            'content': ('尽情书挥洒您的文章'),
        }



class CommentForm(forms.Form):
    content = forms.CharField(label='评论', required=True, )




