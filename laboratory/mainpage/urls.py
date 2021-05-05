from django.urls import path
from .views import BlogListView, BlogDetailView, ProjectDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('posts/<slug:slug>/', BlogDetailView.as_view(), name="post-detail"),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name="project-detail")
]