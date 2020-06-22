from django.contrib import admin

from .models import Contact, Address, Country, Invoice, InvoicePosition

class AddressInLine(admin.StackedInline):
    model = Address
    extra = 0

class InvoicePositionInLine(admin.StackedInline):
    model = InvoicePosition
    extra = 0

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    inlines = [AddressInLine]

    search_fields = ['name']
    list_filter = ['type']
    list_display = ['name', 'type', 'count_addresses']


@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    pass
    search_fields = ['key', 'value']

@admin.register(Invoice)
class AdminInvoice(admin.ModelAdmin):
    inlines = [InvoicePositionInLine]

    search_fields = ['title', 'contact_name']
    list_display = ['title', 'contact_name', 'date', 'due', 'count_invoices']


