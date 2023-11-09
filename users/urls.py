from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, ChangePasswordView, CurrentLoggedInUser, UserDetail
from rest_framework_simplejwt import views as jwt_views


app_name = 'users'

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='register'),

    path('change-password', ChangePasswordView.as_view(), name='register'),
    path(
        'user/', CurrentLoggedInUser.as_view({'get': 'retrieve'}), name="current_user"),
    path('user/<int:pk>/', UserDetail),

    path('token-refresh/',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
