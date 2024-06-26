from django.shortcuts import render
from rest_framework import status , generics
from . import models
from . import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from rest_framework.permissions import IsAuthenticated


# Discount
class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer
    permission_classes = [IsAuthenticated]

# Discount
class DiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer
    permission_classes = [IsAuthenticated]
