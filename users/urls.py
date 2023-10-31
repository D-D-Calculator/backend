from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("login/refresh/", jwt_views.TokenRefreshView.as_view()),
    path("users/", views.UserView.as_view()),
]
