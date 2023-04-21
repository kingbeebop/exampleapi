from rest_framework import serializers
from .models import Lead, Firm

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'from_first', 'from_last', 'from_message', 'from_email', 'from_phone', 'referring_url', 'from_source']


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ['id', 'name', 'api_key', 'inbox_token']