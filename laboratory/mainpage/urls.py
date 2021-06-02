from django.urls import path
from .views import ProjectDetailView
from . import views

urlpatterns = [
    path('', views.mainpage, name='blog'),
    path('posts/', views.posts, name="posts"),
    path('posts/<slug:slug>/', views.post_detail, name='post-detail'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name="project-detail"),
    path('posts/tag/<slug:slug>/', views.tagged, name="tagged"),
]