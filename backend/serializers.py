from rest_framework import serializers

from .models import Contact, Address, Invoice, InvoicePosition, Country

class ContactSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class InvoiceSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoicePositionSerlializer(serializers.ModelSerializer):
    class Meta:
        model = InvoicePosition
        fields = '__all__'

class CountrySerlializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

