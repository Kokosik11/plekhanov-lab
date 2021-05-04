from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('posts/<slug:slug>/', BlogDetailView.as_view(), name="post-detail"),
]