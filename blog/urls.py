from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateview, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateview.as_view(), name='post-update'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]