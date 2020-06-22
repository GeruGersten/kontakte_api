from django.urls import include, path
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactView)
router.register(r'addresses', views.AddressView)
router.register(r'invoices', views.InvoiceView)
router.register(r'invoice_positions', views.InvoicePositionView)
router.register(r'countries', views.CountryView)


urlpatterns = [
    path('', include(router.urls))
]