from django.contrib import admin

from .models import Topic, Article, Comment

# Register your models here.

admin.site.site_header = '简书后台管理系统'
admin.site.index_title = '简书相关信息管理'



'后台注册相关models操作'
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Comment)
