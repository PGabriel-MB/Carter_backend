from rest_framework import serializers

from .models import Address, Contact


class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
