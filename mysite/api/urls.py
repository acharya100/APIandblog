from django.urls import path
from .views import BlogPostListCreateView, BlogPostRetrieveUpdateDestroy, BlogPostList, BlogPostView,KohliView, MessiView, CenaView

urlpatterns = [
    path('blogposts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
    path('blogposts/search/', BlogPostList.as_view(), name='blogpost-search'),
    path('blog/', BlogPostView.as_view(), name='blog-page'),
    path('kohli/', KohliView.as_view(), name='kohli'),
    path('messi/', MessiView.as_view(), name='messi'),
    path('cena/', CenaView.as_view(), name='cena'),
]
