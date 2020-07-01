from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateview
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateview.as_view(), name='post-update'),
    path('about/', views.about, name = 'blog-about'),
]