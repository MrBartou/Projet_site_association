from django.shortcuts import render

@api_view(['GET', 'POST', 'DELETE'])
def backend_list(request):

@api_view(['GET', 'PUT', 'DELETE'])
def backend_detail(request, pk):

@api_view(['GET'])
def backend_list_published(request):