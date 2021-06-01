from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:blog_id>/delete', views.delete, name='delete'),
    path('<int:blog_id>/edit', views.edit, name='edit'),
    path('<int:blog_id>/update', views.update, name='update'),
    path('index/', views.index, name='index'),
    path('introduce/', views.introduce, name='introduce'),
    path('history/', views.history, name='history'),
    path('contact_me/', views.contact_me, name='contact_me'),
    path('favoirte/', views.favorite, name='favorite'),
    
]
