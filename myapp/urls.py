from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('hello/<int:id>', views.hello_id),
    path('hello/<int:id>/<str:name>', views.hello_id_name),
    re_path(r'article/(?P<year>[0-9]{4})/(?P<slag>[\w-]+)$', views.article, name='article'),
]