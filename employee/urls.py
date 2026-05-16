from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import SetPasswordForm, PasswordResetForm

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("register/", views.Register.as_view(), name='register'),
    path("login/", views.Login.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset.html', form_class=PasswordResetForm), name='password_reset'
    ),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'), name='password_reset_done'
    ),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html', form_class=SetPasswordForm
        ), name='password_reset_confirm'
    ),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'), name='password_reset_complete'
    ),
]