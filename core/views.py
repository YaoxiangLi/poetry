from rest_framework import generics

from . import models
from . import serializers


class Ci(generics.ListCreateAPIView):
    queryset = models.Ci.objects.all()
    serializer_class = serializers.CiSerializer


class CiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ci.objects.all()
    serializer_class = serializers.CiSerializer


