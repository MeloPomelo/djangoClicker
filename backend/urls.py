from django.urls import path
from . import views


boosts = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lonely_boost = views.BoostViewSet.as_view({
    'put': 'partial_update',  # Редактировать буст
})
achievements = views.AchievementViewSet.as_view({
    'get': 'list',  # Получить список всех бустов
    'post': 'create',  # Создать буст
})

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.User_login.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('boosts/', boosts, name='boosts'),
    path('boost/<int:pk>/', lonely_boost, name='boost'),
    path('update_coins/', views.update_coins),
    path('core/', views.get_core),
    path('achievements/', achievements, name='achievements'),
]