
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('messages/', views.messages, name = 'blog-messages'),
    path('friends/', views.friends, name = 'blog-friends'),
    path('groups/', views.groups, name = 'blog-groups'),
    path('settings/', views.settings, name = 'blog-settings'),
]
