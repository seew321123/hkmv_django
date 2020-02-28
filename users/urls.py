from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from .views import MyLoginView
from . import views

app_name='users'
urlpatterns = [
    url(r'^login/$', MyLoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^register/$', views.register, name='register'),
]