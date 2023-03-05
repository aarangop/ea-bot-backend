from django.urls import path

from . import views
from .views import PermalinksFileView

app_name = 'ea-bot-api'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('permalinks/', PermalinksFileView.as_view(), name='reddit_permalinks')
]
