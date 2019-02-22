from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, serializer_class, parser_classes
from rest_framework.response import Response
# Create your views here.


@api_view(['POST')
def PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = FileListSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Photo.objects.all()
