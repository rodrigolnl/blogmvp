from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('users/', include('user_api.urls')),
    path('posts/', include('blog_api.urls')),
    path('admin/', admin.site.urls),
]
