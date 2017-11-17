from django.shortcuts import render

from .models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.contrib import auth
from django.db.models import Q
from django.core.urlresolvers import reverse
from .forms import ArticleForm, CommentForm
from datetime import datetime, timedelta
from django.utils import timezone, timesince
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_http_methods

'''
微信test ，，，
'''
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
conf = WechatConf(
    token='',
    appid='wxf54003c617aacd3b',
    appsecret='',
    encrypt_mode='safe',  #可选项：normal/compatible/safe, 分别对应于 明文、兼容、安全 模式
    # encoding_aes_key=''  #（当 Encrypt Mode 为 normal 时无需传入此项）如果传入此值则必须保证同时传入token appid

    # 所有项均可为可选项， 根据自己需要传入对应参数即可。

)
wechat = WechatBasic(conf=conf)


@require_http_methods(['GET', 'POST'])
def show_index(request):
    articles = Article.objects.all()
    topics = Topic.objects.all()[:4]
    return render(request, 'jianshu_app/index.html',
                  {
                    'articles': articles,
                    'topics': topics,
                  })

# 搜索结果页
def search(request):
    result = []
    if request.method == "POST":
        search_name = request.POST.get('search')
        textl = filter(None, search_name.split(' '))
        q = Q()
        for text in textl:
            q |= Q(title__contains = text)
            q |= Q(content__contains = text)
        if len(q) == 0:
            return HttpResponseRedirect(reverse(show_index))

        result = Article.objects.filter(q).all()


    return render(request, 'jianshu_app/search_result.html',
                  {
                      'result': result,
                  })

def get_current_user(request):
    user = request.user
    if user:
        aritcles = user.articles.all()
    return render(request, 'jianshu_app/mine.html',
                  {
                      'user': user,
                      'aritcles': aritcles,
                  })

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm()
        if form.is_valid():
            form.save()
    form = ArticleForm()
    return render(request, 'jianshu_app/edit_aticle.html',
                  {
                      'form': form,
                  })

# 根据时间筛选相应文章
def select_time_article(request, time_id):
    articles = Article.objects.all().filter(Btime__gte=datetime.now() - timedelta(hours=int(time_id))).order_by('views')
    return render(request, 'jianshu_app/select_time_article.html',
                  {
                      'article': articles,
                  })


def show_one_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    articles = topic.articles.all()
    return render(request, 'jianshu_app/topic.html',
                  {
                      'topic': topic,
                      'articles': articles,
                  })


def show_all_topics(request):
    topics = Topic.objects.all()
    return render(request, 'jianshu_app/topics.html',
                  {
                      'topics': topics,
                  })

def show_one_article(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
        print(request.user)
        print(request.user.username, request.user.is_active)
        article = get_object_or_404(Article, pk=article_id)

        Comment.objects.create(owner=request.user, article=article, content=content, star=1)

    article = get_object_or_404(Article, pk=article_id)
    article.add_one_count()
    comments = article.comments_to_article.all()
    return render(request, 'jianshu_app/article_detail.html',
                  {
                      'article': article,
                      'comments': comments,
                      'form': CommentForm(),
                  })

# ajax 返回评论信息
def show_article_all_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments_to_article.all()
    if comments is not None:
        return JsonResponse({
            'code': 0 ,
            'result': [
                {
                    'comment_id': comment.id,
                    'content': comment.content,
                    'time': comment.btime,
                    'uid': comment.owner.id,
                    'username': comment.owner.username,
                }
                for comment in comments
            ],
        })
    else:
        return HttpResponseBadRequest()

# ajax 增加新的评论信息
def add_article_comment(request, article_id):
    # print('i' * 40)
    # print(request.user.username)
    # print('e' * 44)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        # if form.is_valid():
        #     content = form.cleaned_data('content')
        # print(content)
        content = request.POST.get('content')
        print(content)
        print('1####'*10)

        article = get_object_or_404(Article, pk=article_id)
        new_comment = Comment.objects.create(owner=request.user, article=article, content='456789', star=1)
        return JsonResponse({
            'code': 0,
            'result':
                {
                    'comment_id': new_comment.id,
                    'content': new_comment.content,
                    'time': new_comment.btime,
                    'uid': new_comment.owner.id,
                    'username': new_comment.owner.username,
                },
        })


# 原生的 展示用户评论
@login_required
def show_article_comment(request, article_id, stars):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data('content')
        user = request.user
        article = get_object_or_404(Article, pk=article_id)
        # user = article.user

        Comment.objects.create(owner=user, article=article, content=content, stars=stars)

        print('-8-' * 20)

    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.all()

    return render(request, 'jianshu_app/article_detail.html',
                  {
                      'article': article,
                      'comments': comments,
                  })




# 注册
@csrf_exempt
def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')

        if not request.POST.get('password2'):
            errors.append('确认密码不能为空')
        else:
            password2 = request.POST.get('password2')

        if not request.POST.get('email'):
            errors.append('邮箱不能为空')
        else:
            email = request.POST.get('email')

        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('两次输入密码不一致')

        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag:
            user = User.objects.create_user(account, email, password)
            user.save()

            userlogin = auth.authenticate(username = account, password = password)
            auth.login(request, userlogin)
            return HttpResponseRedirect('/')

    return render(request, 'jianshu_app/register.html',
                  {
                      'errors': errors
                  })


# 用户登录
def my_login(request):
    errors = []
    account = None
    password = None
    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')


        if account is not None and password is not None:
            user = auth.authenticate(username = account, password = password)
            if user is not  None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    errors.append('用户名错误')
            else:
                errors.append('用户名或密码错误')

    return render(request, 'jianshu_app/login.html',
                  {
                      'errors': errors
                  })


def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


