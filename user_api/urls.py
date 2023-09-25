from django.urls import path
from .views import RegisterViewSet, UserViewSet, UsersViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', UsersViewSet.as_view()),
    path('user/', UserViewSet.as_view()),
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]