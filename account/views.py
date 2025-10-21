from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils import timezone
from .serializers import RegisterSerializer, ProfileSerializer
from .models import CustomUser
from audit.models import LoginLog
from django.shortcuts import get_object_or_404, redirect


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            try:
                user = CustomUser.objects.get(email=request.data.get("email"))
                # Логируем в отдельную базу audit
                LoginLog.objects.using("audit").create(
                    user_id=user.id,
                    user_email=user.email,
                    timestamp=timezone.now(),
                    ip_address=request.META.get("REMOTE_ADDR"),
                    user_agent=request.META.get("HTTP_USER_AGENT", ""),
                )
            except CustomUser.DoesNotExist:
                pass
        return response

class ActivateView(APIView):
    def get(self, request, ):
        activation_code = request.query_params.get('u')
        user = get_object_or_404(CustomUser, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ""
        user.save()
        return redirect('https://google.com')