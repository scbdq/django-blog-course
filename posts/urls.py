from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail_view, name='post_detail'),
]
