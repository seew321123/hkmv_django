from django.urls import path
from django.conf.urls import url
from . import views

app_name='movies'
urlpatterns = [
    path('', views.movies, name='movies'),
    url(r'^(?P<movie_id>\d+)/$', views.comment, name = 'comment'),
    url(r'^ajax_test/(?P<comment_id>\S+)/$', views.ajax_test, name = 'ajax_test'),
    url(r'^add_comment/(?P<movie_id>\d+)/$', views.add_comment, name = 'add_comment'),
    url(r'^add_comment_in_comment/(?P<comment_id>\S+)/$', views.add_comment_in_comment, name='add_comment_in_comment'),
    url(r'^edit_comment/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment'),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', views.delete_comment, name='delete_comment'),
    path('user_center', views.user_center, name='user_center'),
    url(r'^like/(?P<comment_id>\S+)/$', views.like, name = 'like'),
    url(r'^refresh/(?P<comment_id>\S+)/$', views.refresh, name = 'refresh'),
    url(r'^refresh/(?P<comment_id>\S+)/$', views.refresh, name = 'refresh'),
    path('search_movie', views.search_movie, name='search_movie'),
]