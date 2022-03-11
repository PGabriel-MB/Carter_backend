from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class ForgotPassword(APIView):

    def post(self, request, format=None):

        email = request.data['email']

        if not email:
            return Response(
                {'error': 'O campo e-mail é obrigatório!'},
                status=400
            )
        
        user = User.objects.filter(email=email).first()

        if not user:
            return Response(
                {'error': 'Este usuário não existe!'}
            )

        

        return Response({ 'msg': f'{email}'})
