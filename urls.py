from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('create/', views.create_post, name='create_post'),
    path('comment/<int:post_id>/', views.comment_post, name='comment_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
