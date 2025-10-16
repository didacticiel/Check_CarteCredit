# credit_check/urls.py
from django.urls import path
from . import views

app_name = "credit_check"
urlpatterns = [
    path("", views.home, name="home"),
    path("api/check/", views.api_check_card, name="api_check"),
]
