from django.urls import path
from .views import BlogPostViewSet, AllBlogPostViewSet


urlpatterns = [
    path('', BlogPostViewSet.as_view(http_method_names=['post'])),
    path('<uuid:pk>/', BlogPostViewSet.as_view()),
    path('all/', AllBlogPostViewSet.as_view()),
]