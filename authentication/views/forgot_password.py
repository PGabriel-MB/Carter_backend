from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class ForgotPassword(APIView):

    def post(self, request, format=None):

        email = request.data['email']
        username = request.data['username']

        return Response({ 'msg': f'{email} {username}'})
