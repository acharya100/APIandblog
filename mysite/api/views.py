from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.views import View

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', '')
        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogPostView(View):
    def get(self, request):
        blog_posts = BlogPost.objects.all().order_by('-published_date')
        return render(request, 'api/blog.html', {'blog_posts': blog_posts})

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            BlogPost.objects.create(title=title, content=content)
        return redirect('blog-page')

class KohliView(View):
    def get(self, request):
        return render(request, 'api/kohli.html')

class MessiView(View):
    def get(self, request):
        return render(request, 'api/messi.html')

class CenaView(View):
    def get(self, request):
        return render(request, 'api/cena.html')