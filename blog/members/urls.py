from django.urls import path
from .views import UserRegistrationView, UserSettingsEditView, ChangePasswordView, ShowProfilePageView, EditProfilePageView
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('edit_user_settings/', UserSettingsEditView.as_view(), name = 'edit_user_settings'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', ChangePasswordView.as_view(), name = 'change_password'),
    path('password_success/', views.password_success, name = 'password_success'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name = 'show_profile_page'),
    path('edit_profile/<int:pk>', EditProfilePageView.as_view(), name = 'edit_profile_page')
]