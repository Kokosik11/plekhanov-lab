from django.urls import path
from .views import RegisterView, ProfileView
from django.contrib.auth import views as auth_views
from .forms import UserAuthentication

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('account/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=UserAuthentication), name='login'),
    path('exit/', auth_views.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
]