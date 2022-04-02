from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import login_view, logout_view, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="registration")

]