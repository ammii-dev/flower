
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, PermissionDenied
from core.models import Escort

from escort import serializers


class EscortsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    queryset = Escort.objects.all()
    serializer_class = serializers.EscortsSerializer


class EscortViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """Manage tags in the database"""
    queryset = Escort.objects.all()
    serializer_class = serializers.EscortsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostEscortsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Escort.objects.all()
    serializer_class = serializers.EscortsSerializer

    def perform_create(self, serializer):
        """Create a new ingredient"""
        queryset = Escort.objects.filter(user=self.request.user)
        if queryset.exists():
            raise APIException('You have already posted')
        serializer.save(user=self.request.user)

class EditEscortViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Escort.objects.all()
    serializer_class = serializers.EscortsSerializer

    def perform_update(self, serializer):
        """Create a new ingredient"""
        try:
            queryset = Escort.objects.filter(user=self.request.user)
            if not queryset.exists():
                raise APIException('Dose not have escort post')
            serializer.save(user=self.request.user)
        except:
            raise PermissionDenied('Not allow to access')
