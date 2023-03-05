from django.urls import path

from . import views

app_name = 'ea-bot-api'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<pk>', views.PostDetailView.as_view(), name='post_detail')
]
