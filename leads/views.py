from django.http import JsonResponse
from .models import Lead, Firm
from .serializers import LeadSerializer, FirmSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

#/leads/ display json of all leads
#intended for internal use only
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
#intended for internal use only
@api_view(['GET', 'POST', 'DELETE'])
def lead_detail(request, id):
    
    try:
        lead = Lead.objects.get(pk=id)
    except Lead.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LeadSerializer(lead)
        return Response({"inbox_lead": serializer.data, "inbox_token": lead.firm.inbox_token})
    elif request.method == 'POST':
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#/inbox/api_key
@api_view(['GET'])
def lead_inbox(request, api_key):

    #api validation, find firm by api key
    #not secure
    #TODO: use built in api keys instead
    try:
        firm = Firm.objects.get(api_key = api_key)
    except Firm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        try:
            lead = Lead.objects.get(firm = firm, processed = False)
            print(lead)
        except Lead.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        #serialize data
        serializer = LeadSerializer(lead)

        #TODO:
        #This fetch request isn't currently accepted by clio
        #as per their documentation, api requests typically are sent with an authentication token
        #but could not find authentication on the test server enviornment
        #Thinking that perhaps clio has whitelisted the server to allow for the old VB code to work
        #Need to test once enviornment is properly configured
        #OR need to get information to generate a new authentication token for this fetch to go through
        #/////
        #send POST request to clio with message data
        clio_response = requests.post(
            'https://grow.clio.com/inbox_leads',
            data = {"inbox_lead": serializer.data,
                    "inbox_token": firm.inbox_token},
                    headers = {"Content-Type": "application/json",
                               "Accept": "application/json"})
        
        #if 202 response, mark new message as processed
        if clio_response.status_code == 202:
            lead.processed = True
            lead.save()
        
        #return json with sent data and a copy of the response from the clio api call above
        return Response({"data": {"inbox_lead": serializer.data, "inbox_token": firm.inbox_token}, "response": clio_response})