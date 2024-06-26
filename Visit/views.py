from django.shortcuts import render
from rest_framework import status , generics
from . import models
from . import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from rest_framework.permissions import IsAuthenticated


# Visit
class VisitListCreateView(generics.ListCreateAPIView):
    queryset = models.Visit.objects.all()
    serializer_class = serializers.VisitSerializer
    permission_classes = [IsAuthenticated]

# Visit
class VisitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Visit.objects.all()
    serializer_class = serializers.VisitSerializer
    permission_classes = [IsAuthenticated]



# Question
class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [IsAuthenticated]

# Question
class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [IsAuthenticated]





# KindOfCounseling
class KindOfCounselingListCreateView(generics.ListCreateAPIView):
    queryset = models.KindOfCounseling.objects.all()
    serializer_class = serializers.KindOfCounselingSerializer
    permission_classes = [IsAuthenticated]

# KindOfCounseling
class KindOfCounselingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.KindOfCounseling.objects.all()
    serializer_class = serializers.KindOfCounselingSerializer
    permission_classes = [IsAuthenticated]


