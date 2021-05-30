from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('singup/', views.signup, 'signup'),
    path('login/', views.login, 'login'),
    path('logout/', views.logout, 'logout'),
    path('mypage/', views.mypage, 'mypage'),
]
