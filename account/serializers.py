from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create(password=password, **validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username", "first_name", "last_name")
