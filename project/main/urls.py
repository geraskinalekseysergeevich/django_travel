from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('post1/', views.post1, name='post1'),
    path('post2/', views.post2, name='post2'),
    path('post3/', views.post3, name='post3'),
    path('task/', views.calculate, name='task')
]