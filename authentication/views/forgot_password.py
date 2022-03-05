from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class ForgotPassword(APIView):
    def post(self, request, *args, **kwargs):
        email, username = request.data

        print(email)
        print(username)

        return Response({ 'msg': 'Deu bomm, ou quase' })
