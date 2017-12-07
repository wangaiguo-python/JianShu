from django.contrib import admin

from .models import Topic, Article, Comment
from django.http import HttpResponse
import datetime
import csv
from .commen import export_as_csv_action

# Register your models here.

admin.site.site_header = '简书后台管理系统'
admin.site.index_title = '简书相关信息管理'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'views', 'likes', 'Btime']
    actions = [export_as_csv_action("导出表格", fields=['title', 'views', 'likes', 'Btime'])]



'后台注册相关models操作'
admin.site.register(Topic)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
