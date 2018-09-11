from rest_framework import serializers
from .models import AccountInvoice

class AccountInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountInvoice
        fields='__all__'
