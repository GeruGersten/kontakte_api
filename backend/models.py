from django.db import models
import datetime

TYPE_CHOICE = (
    ('Privat', 'Privat'),
    ('Company', 'Company')
)

class Contact(models.Model):
    type = models.CharField(max_length=20, choices=TYPE_CHOICE, default='Privat')
    name = models.CharField(max_length=256,
                           help_text = 'Firmenname oder Vor- und Nachname')
    email = models.EmailField(max_length=256)
    salutation = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    @property
    def count_addresses(self):
        return self.addresses.count()

class Address(models.Model):
    street = models.CharField(("Strasse"),max_length=256)
    zip = models.CharField(("PLZ"),max_length=10)
    city = models.CharField(("Stadt"),max_length=256)

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='addresses')
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.contact.type, self.contact.name)

class Country(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.CharField(("Land"),max_length=256)

    def __str__(self):
        return self.value

class Invoice(models.Model):
    title = models.CharField(("Rechnung"),max_length=256)
    body = models.TextField(("Beschreibung"), blank=True)
    due = models.DateField(("Fällig"), default=datetime.date.today)
    date = models.DateField(("Datum"), default=datetime.date.today)
    conditions = models.CharField(("Konditionen"), max_length=256)

    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def contact_name(self):
        return self.address

    @property
    def count_invoices(self):
        return self.invoices.count()

class InvoicePosition(models.Model):
    title = models.CharField(("Titel"), max_length=256)
    body = models.TextField(("Beschreibung"), blank=True)
    quantity = models.PositiveIntegerField(("Menge"), default=1)
    amount = models.DecimalField(("Betrag CHF"),max_digits=5, decimal_places=2)

    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='invoices')

    def __str__(self):
        return self.title