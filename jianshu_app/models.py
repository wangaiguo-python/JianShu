from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core import validators



class Topic(models.Model):
    name = models.CharField('名称', max_length=20)
    img = models.ImageField('封面', )
    Btime = models.DateTimeField('创建时间', default=timezone.now,)


    class Meta:
        verbose_name_plural = verbose_name = '专题'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.name}'

class Article(models.Model):
    title = models.CharField('名称', max_length=128)
    cover = models.ImageField('封面', )
    content = UEditorField(u'内容 ', width=1000, height=300, toolbars="full", imagePath="", filePath="",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None, blank=True)
    views = models.IntegerField('阅读量', default=0)
    likes = models.IntegerField('喜欢数', default=0)
    comments = models.IntegerField('评论数', default=0)
    topic = models.ForeignKey(Topic, related_name='articles', verbose_name='专题')
    user = models.ForeignKey('auth.User', related_name='articles', verbose_name='用户')
    Btime = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '文章'

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.__class__.__name__} - {self.__str__()}'

    def add_one_count(self):
        self.views += 1
        self.save()   # 有时候就是一种尝试而已


class Comment(models.Model):
    content = models.CharField('评论内容', max_length=2048)
    article = models.ForeignKey(Article, verbose_name='文章', related_name='comments_to_article')
    owner = models.ForeignKey(User, verbose_name='评论人', related_name='comment_to_owner')

    # 这个有可能造成一个递归的死循环
    # comments_to_comment = models.ForeignKey('self', verbose_name='对于评论的评论', related_name='comments_to_comment')

    btime = models.DateTimeField('评论时间', auto_now_add=True)

    # 外带的评论附加限制条件 ， 防止评论无限循环下去
    star = models.IntegerField('评级', validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5),])

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return f'{self.content}'[:20]

    def __repr__(self):
        return f'{self.__class__.__name__}-{self.__str__()}'



# class TestArticle(models.Model):
#     title = models.CharField('名称', max_length=128)
#     content = models.TextField('内容' )
#     views = models.IntegerField('阅读量', default=0)
#     likes = models.IntegerField('喜欢数', default=0)
#     comments = models.IntegerField('评论数', default=0)
#     cover = models.ImageField('封面', )
#     topic = models.ForeignKey(Topic, related_name='articles', verbose_name='专题')
#
#     class Meta:
#         verbose_name_plural = verbose_name = '文章'
#
#     def __str__(self):
#         return f'{self.title}'
#
#     def __repr__(self):
#         return f'{self.__class__.__name__} {self.__str__()}'
#
# class UArticle(models.Model):
#     # content = UEditorField('内容', height=300, width=1000, default='', blank=True,
#     #                        imagePath='', toolbars='besttome', filePath='')
#     content = UEditorField(u'内容 ', width=1000, height=300, toolbars="full", imagePath="", filePath="",
#                            upload_settings={"imageMaxSize": 1204000},
#                            settings={}, command=None, blank=True)
#
#     class Meta:
#         verbose_name_plural = verbose_name = '富文本编辑'
#
#     def __str__(self):
#         return f'{self.content[:10]}'
#
#     def __repr__(self):
#         return f'{self.__class__.__name__} {self.__str__()}'
#
#     def get_absolute_url(self):
#         return reverse('id', args=(self.content, ))
