from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from ..serializers import CompanySerializer
from base.serializers import AddressSerializer, ContactSerializer


class SimpleAddCompanyCreate(CreateModelMixin, GenericAPIView):
    serializer_class = CompanySerializer

    def post(self, request, *args, **kwargs):
        contact_data = request.data['contact']
        request.data.pop('contact', None)
        address_data = request.data['address']
        request.data.pop('address', None)

        contact_serializer = ContactSerializer(data=contact_data)
        contact_serializer.is_valid(raise_exception=True)
        contact_serializer.save()

        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'msg': 'Mensagem de retorno'})
