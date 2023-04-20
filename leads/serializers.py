from rest_framework import serializers
from .models import Lead, Firm

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'first_name', 'last_name', 'message', 'email', 'phone', 'url', 'source', 'processed']


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ['id', 'name', 'api_key', 'inbox_token']