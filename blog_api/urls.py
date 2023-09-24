from django.urls import path
from .views import BlogPostView, AllBlogPostView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', BlogPostView.as_view(http_method_names=['post'])),
    path('<uuid:pk>/', BlogPostView.as_view()),
    path('all/', AllBlogPostView.as_view()),
]