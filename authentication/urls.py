from django.urls import path

from .views import CustomAuthToken, ForgotPassword


urlpatterns = [
    path('', CustomAuthToken.as_view()),
    path('forget-password', ForgotPassword.as_view())
]