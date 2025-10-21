from django.db import models

class LoginLog(models.Model):
    user_id = models.IntegerField()  # id из базы account
    user_email = models.EmailField(null=True, blank=True)
    # email пользователя
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)

    class Meta:
        app_label = "audit"
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.user_email} — {self.timestamp}"
