from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, ProfileView, CustomTokenObtainPairView, ActivateView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("me/", ProfileView.as_view()),
    path("token/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path('activate/', ActivateView.as_view()),
]
