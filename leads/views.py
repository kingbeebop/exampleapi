from django.http import JsonResponse
from .models import Lead, Firm
from .serializers import LeadSerializer, FirmSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#/leads/ display json of all leads
@api_view(['GET', 'POST'])
def lead_list(request):

    if request.method == 'GET':
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LeadSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#/leads/id get, update, delete requests
@api_view(['GET', 'PUT', 'DELETE'])
def lead_detail(request, id):
    
    try:
        lead = Lead.objects.get(pk=id)
        firm = Firm.objects.get(pk=lead.firm.id)
    except Lead.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LeadSerializer(lead)
        return Response({"inbox_lead": serializer.data, "inbox_token": firm.inbox_token})
    elif request.method == 'PUT':
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)