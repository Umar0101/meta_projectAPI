from django.urls import path
from .views import LoginLogListView

urlpatterns = [
    path("login/", LoginLogListView.as_view()),
]
