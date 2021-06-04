from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class PartnershipViewSet(viewsets.ModelViewSet):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer

class SubsciptionViewSet(viewsets.ModelViewSet):
    queryset = Subsciption.objects.all()
    serializer_class = SubsciptionSerializer

class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer

@api_view(['POST'])
def activity_list(request):
    if request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def suppr_acti(request, title):
    try:
        even = Events.objects.get(title=title)
    except Events.DoesNotExist:
        return JsonResponse({'message': 'The Events does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        even.delete()
        return JsonResponse({'message': 'Events was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def user_list(request):
    if request.method == 'POST':
        serializer = SubsciptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def partnership_list(request):
    if request.method == 'POST':
        serializer = PartnershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)