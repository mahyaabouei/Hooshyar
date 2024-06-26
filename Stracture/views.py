from django.shortcuts import render
from rest_framework import status , generics
from . import models
from . import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from rest_framework.permissions import IsAuthenticated


# SelectTime
class SelectTimeListCreateView(generics.ListCreateAPIView):
    queryset = models.SelectTime.objects.all()
    serializer_class = serializers.SelectTimeSerializer
    permission_classes = [IsAuthenticated]

# SelectTime
class SelectTimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SelectTime.objects.all()
    serializer_class = serializers.SelectTimeSerializer
    permission_classes = [IsAuthenticated]


