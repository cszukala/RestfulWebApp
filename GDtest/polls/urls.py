from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='poll-home'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='poll-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='poll-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='poll-delete'),
    path('post/new/', PostCreateView.as_view(), name='poll-create'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('about/', views.about, name='poll-about'),
]