from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Contact, Address, Invoice, InvoicePosition, Country
from .serializers import ContactSerlializer, AddressSerlializer, InvoiceSerlializer, InvoicePositionSerlializer, CountrySerlializer

class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerlializer
    queryset = Contact.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerlializer
    queryset = Address.objects.all()

class InvoiceView(viewsets.ModelViewSet):
    serializer_class = InvoiceSerlializer
    queryset = Invoice.objects.all()

class InvoicePositionView(viewsets.ModelViewSet):
    serializer_class = InvoicePositionSerlializer
    queryset = InvoicePosition.objects.all()

class CountryView(viewsets.ModelViewSet):
    serializer_class = CountrySerlializer
    queryset = Country.objects.all()