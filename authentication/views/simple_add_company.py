from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from ..serializers import CompanySerializer


class SimpleAddCompanyCreate(CreateModelMixin, GenericAPIView):
    serializer_class = CompanySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'msg': 'Mensagem de retorno'})
