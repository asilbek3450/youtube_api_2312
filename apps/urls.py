from .views import UserListCreateAPIView, UserDetailAPIView, VideoListCreateAPIView, VideoDetailAPIView, ChannelListCreateAPIView, ChannelDetailAPIView
from django.urls import path

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('videos/', VideoListCreateAPIView.as_view(), name='video_list'),
    path('videos/<int:pk>/', VideoDetailAPIView.as_view(), name='video_detail'),
    path('channels/', ChannelListCreateAPIView.as_view(), name='channel_list'),
    path('channels/<int:pk>/', ChannelDetailAPIView.as_view(), name='channel_detail'),
]
