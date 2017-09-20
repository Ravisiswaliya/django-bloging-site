from django.conf.urls import url
from . import views
app_name = 'news'
urlpatterns = [
        url(r'^$',views.home, name='home'),
        url(r'^news_list', views.news_list, name='news_list'),
        url(r'^news/(?P<id>\d+)/$', views.news_detail, name="news_detail"),
        url(r'^create_news', views.create_news, name='create_news'),
        url(r'^delete/(?P<id>\d+)/$', views.delete_news, name='delete'),
        url(r'^update/(?P<id>\d+)/$', views.update_news, name='update'),

]