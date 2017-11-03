
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.my_login, name='my_login'),
    url(r'^logout/$', views.my_logout, name='my_logout'),
    url(r'^search/$', views.search, name="search"),
    url(r'^mine/$', views.get_current_user, name='mine'),
    url(r'^editArticle/$', views.create_article, name='editArticle'),
    url(r'^article_time_contains/([^/]+)/$', views.select_time_article, name='select_time'),
    url(r'^all_topics/$', views.show_all_topics, name='show_all_topics'),
    url(r'^topic=([^/]+)/$', views.show_one_topic, name='show_one_topic'),
    url(r'^article/id=([^/]+)/$', views.show_one_article, name='show_one_article'),
    url(r'^article/id=([^/]+)/comments/$', views.show_article_all_comment, name='show_article_all_comment'),
    url(r'^article/id=([^/]+)/new_comment/$', views.add_article_comment, name='add_article_comment'),
    url(r'^comment/article_id=([^/]+)/stars=([^/]+)/$', views.show_article_comment, name='show_article_comment'),
]


