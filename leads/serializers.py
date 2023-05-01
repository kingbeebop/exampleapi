from rest_framework import serializers
from .models import Lead, Firm

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'message', 'email', 'phone', 'url', 'source']

class ClioSerializer(serializers.ModelSerializer):

    from_first = serializers.CharField(source = 'first_name')
    from_last = serializers.CharField(source = 'last_name')
    from_message = serializers.CharField(source = 'message')
    from_email = serializers.EmailField(source = 'email')
    from_phone = serializers.CharField(source = 'phone')
    referring_url = serializers.CharField(source = 'url')
    from_source = serializers.CharField(source = 'source')

    class Meta:
        model = Lead
        fields = ['from_first', 'from_last', 'from_message', 'from_email', 'from_phone', 'referring_url', 'from_source']


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ['id', 'name', 'api_key', 'inbox_token']