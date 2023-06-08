from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from ..serializers import CompanySerializer
from base.serializers import AddressSerializer, ContactSerializer


class SimpleAddCompanyCreate(CreateModelMixin, GenericAPIView):
    serializer_class = CompanySerializer

    def post(self, request, *args, **kwargs):
        contact_data = request.data['contact']
        request.data.pop('contact', None)
        address_data = request.data['address']
        request.data.pop('address', None)

        try:
            contact_serializer = ContactSerializer(data=contact_data)
            contact_serializer.is_valid(raise_exception=True)
            new_contact = contact_serializer.save()

            address_serializer = AddressSerializer(data=address_data)
            address_serializer.is_valid(raise_exception=True)
            new_address = address_serializer.save()

            request.data['contact'] = new_contact.id
            request.data['address'] = new_address.id

        except Exception as e:
            return Response({'error': e})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'success': _('Company created Successfully!')})
