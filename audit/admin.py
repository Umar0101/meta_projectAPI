from django.contrib import admin
from .models import LoginLog

@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_email", "timestamp", "ip_address", "user_agent")
    list_filter = ("timestamp",)
    search_fields = ("user_email", "ip_address", "user_agent")
    ordering = ("-timestamp",)
