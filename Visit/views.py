from django.shortcuts import render
from rest_framework import status , generics
from . import models
from . import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from Authentication import fun
from Authentication.serializers import UserSerializer , ConsultantSerializer
from Stracture.serializers import SelectTimeSerializer


# Visit
class VisitViewset(APIView):

    def post(self, request):
            Authorization = request.headers.get('Authorization')
            if not Authorization:
                return Response({'error': 'Authorization header is missing'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = fun.decryptionUser(Authorization)
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            user = user.first()  
            consultant = models.Consultant.objects.filter(id = request.data.get('consultant'))
            if not consultant.exists ():
                return Response('no consultant', status=status.HTTP_400_BAD_REQUEST)
            consultant = consultant.first()
            serializer_consultant = ConsultantSerializer(consultant,)
            question = request.data.get('questions')
            question_model = models.Question(
                question_1 = question['0'] ,
                question_2 = question['1'] ,
                question_3 = question['2'] ,
                question_4 = question['3'] ,
                question_5 = question['4'] ,
                question_6 = question['5'] ,
                question_7 = question['6'] ,
                question_8 = question['7'] ,
                question_9 = question['8'] ,
                question_10 = question['9'] )
            question_model.save()
            serializer_question = serializers.QuestionSerializer(question_model)


            kind = models.KindOfCounseling.objects.filter(id= request.data.get ('kind'))
            if not kind.exists() :
                return Response ('no kind', status=status.HTTP_400_BAD_REQUEST)
            kind = kind.first()
            serializer_kind = serializers.KindOfCounselingSerializer (kind)

            date_str = request.data.get('date')
            time = request.data.get ('time')
            if not date_str:
                return Response({'error': 'No date provided'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                date_str = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
            except:
                return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)
            date = models.SelectTime.objects.filter(date =date_str , time =time , reserve = False )
            if not date.exists () :
                return Response ({'no date'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            date = date.first()

            visit_model = models.Visit(customer=user , consultant =consultant  ,kind = kind, questions = question_model , date = date)
            visit_model.save()
            models.SelectTime.objects.filter(id=date.id).update(reserve=True)
            
            return Response({'ok'}, status=status.HTTP_201_CREATED)


    def get(self, request):
    
        Authorization = request.headers.get('Authorization')
        if not Authorization:
            return Response({'error': 'Authorization header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = fun.decryptionUser(Authorization)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user_instance = user.first()
        visits = models.Visit.objects.filter(customer=user_instance)
        
        if not visits.exists():
            return Response({'message' : 'کاربر ویزیت ندارد'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.VisitSerializer(visits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Question

class QuestionViewset(APIView):

    def post (self, request) :
        Authorization = request.headers.get('Authorization')
        if not Authorization :
            return Response({'error': 'Authorization header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        user = fun.decryptionUser(Authorization)
        if not user :
            return Response({'error' : 'User not found'} , status=status.HTTP_404_NOT_FOUND)
        user_instance = user.first()
        data = request.data.copy()
        data ['title'] = user_instance.id 
        serializer = serializers.QuestionSerializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get (self, request) :
        Authorization = request.headers.get('Authorization')
        if not Authorization :
            return Response({'error': 'Authorization header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        user = fun.decryptionUser(Authorization)
        if not user :
            return Response({'error' : 'User not found'} , status=status.HTTP_404_NOT_FOUND)
        user_instance = user.first()
        question = models.Question.objects.all()
        if not question.exists () :
            return Response ([],status=status.HTTP_200_OK)
        serializer = serializers.QuestionSerializer(question , many = True)
        return Response (serializer.data , status=status.HTTP_200_OK)




# Kind Of Counseling
class KindOfCounselingViewset(APIView):
    
    def get(self, request):
        Authorization = request.headers.get('Authorization')
        if not Authorization:
            return Response({'error': 'Authorization header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = fun.decryptionUser(Authorization)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
        kind = models.KindOfCounseling.objects.all()
        if not kind.exists():
            return Response([], status=status.HTTP_200_OK)
        
        serializer = serializers.KindOfCounselingSerializer(kind, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





# Visit Profile 
class VisitProfileView(APIView):
    def get(self , request):
        Authorization = request.headers['Authorization']
        if not Authorization:
            return Response({'error': 'Authorization header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = fun.decryptionUser(Authorization)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user_instance = user.first()
        serializer = serializers.VisitSerializer(user_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)



