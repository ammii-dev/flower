from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from escorts.models import EscortPost
from escorts.serializers import EscortSerializer

@api_view(['GET'])
def escort_list(request):
    """
    List all escorts.
    """
    if request.method == 'GET':
        escort = EscortPost.objects.all()
        serializer = EscortSerializer(escort, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_escort(request):
    """
    Create a new Escort.
    """
    if request.method == 'POST':
        serializer = EscortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def escort_detail(request, pk):
    """
    Retrieve, update or delete a Escort.
    """
    try:
        escort = Escorts.objects.get(pk=pk)
    except Escorts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EscortSerializer(escort)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        escort.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def edit_escort(request, pk):
    """
    Update a Escort.
    """
    try:
        escort = Escorts.objects.get(pk=pk)
    except Escorts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EscortSerializer(escort, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
