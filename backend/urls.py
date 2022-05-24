from django.urls import path
from . import views


boosts = views.BoostViewSet.as_view({
    'get': 'list',  # Получить список всех бустов
    'post': 'create',  # Создать буст
})


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.User_login.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('call_click/', views.call_click),
    path('boosts/', boosts, name='boosts'),
]