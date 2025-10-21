from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import LoginLog
from .serializers import LoginLogSerializer


class LoginLogListView(generics.ListAPIView):
    queryset = LoginLog.objects.using("audit").all()
    serializer_class = LoginLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["user_email", "timestamp"]
    ordering_fields = ["timestamp"]

    def get_queryset(self):
        return LoginLog.objects.using("audit").filter(user_email=self.request.user.email)