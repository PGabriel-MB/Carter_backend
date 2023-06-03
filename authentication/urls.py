from django.urls import path

from .views import CustomAuthToken, ForgotPassword, SimpleAddCompanyCreate


urlpatterns = [
    path('', CustomAuthToken.as_view()),
    path('forgot-password', ForgotPassword.as_view()),
    path('simple-add-company', SimpleAddCompanyCreate.as_view())
]
