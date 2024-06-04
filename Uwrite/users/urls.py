from django.urls import path
from .views import register, profile, author_profile
from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [
    # http://127.0.0.1:8000/users/
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name='users/logout.html', next_page="users:login"), name="logout"),
    path("profile/", profile, name="profile"),
    path("author_profile/<int:id>/", author_profile, name="author_profile"),
]