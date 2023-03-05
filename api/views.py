from django.http import JsonResponse
from django.views import View
from rest_framework import generics

from .models import Post, PermalinksFile
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PermalinksFileView(View):

    def get(self, request):
        posts = PermalinksFile.download_permalinks_file()
        return JsonResponse({'posts': posts})
