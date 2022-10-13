from django.urls import path
from . import views

# app_name: URL을 변수화 해서 사용
app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("<int:pk>/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
]
