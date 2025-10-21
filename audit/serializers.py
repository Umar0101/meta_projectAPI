from rest_framework import serializers
from .models import LoginLog


class LoginLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginLog
        fields = "__all__"
