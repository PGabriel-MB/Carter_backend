from django.urls import path

from .views import CustomAuthToken, ForgotPassword


urlpatterns = [
    path('', CustomAuthToken.as_view()),
    path('forgot-password', ForgotPassword.as_view())
]