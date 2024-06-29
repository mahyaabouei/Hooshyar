from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
from GuardPyCaptcha.Captch import GuardPyCaptcha
from . import models
from . import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from . import fun
class CaptchaViewset (APIView) :
    def get (self , request) :
        captcha = GuardPyCaptcha()
        captcha = captcha.Captcha_generation (num_char = 4 , only_num = True) 
        return Response (captcha , status = status.HTTP_200_OK)
    

class OtpViewset  (APIView) :
    def post (self , request) : 
        captcha = GuardPyCaptcha ()

        captcha = captcha.check_response (request.data ['encrypted_response'],request.data ['captcha'] )
        if False :
            result = {'message' : 'کد کپچا صحیح نیست'}
            return Response (result , status= status.HTTP_406_NOT_ACCEPTABLE)
        mobile = request.data ['mobile']
        if not mobile:
            return Response({'message': 'شماره همراه لازم است'}, status=status.HTTP_400_BAD_REQUEST)
        try :
            user = models.Auth.objects.get(mobile = mobile)
            result = {'registered' : True , 'message' : 'کد تایید ارسال شد'}    

        except models.Auth.DoesNotExist: 
            result = {'registered' : False , 'message' : 'کد تایید ارسال شد'}    

        code = 11111 #random.randint(10000,99999)
        otp = models.Otp(mobile=mobile,code =code)
        otp.save()

        return Response(result,status=status.HTTP_200_OK)


class LoginViewset (APIView) :
    def post (self,request) :
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        
        if not mobile or not code:
            return Response({'message': 'شماره همراه و کد تأیید لازم است'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = models.Auth.objects.get(mobile=mobile)
        except:
            result = {'message': ' شماره موبایل موجود نیست لطفا ثبت نام کنید'}
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        
        try:
            otp_obj = models.Otp.objects.filter(mobile=mobile , code = code ).order_by('-date').first()
        except :
            
            return Response({'message': 'کد تأیید نامعتبر است'}, status=status.HTTP_400_BAD_REQUEST)
        
        otp = serializers.OtpSerializer(otp_obj).data
        if otp['code']== None :
            result = {'message': 'کد تأیید نامعتبر است'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
            
        otp = serializers.OtpSerializer(otp_obj).data
        dt = datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(otp['date'].replace("Z", "+00:00"))
        
        dt = dt.total_seconds()

        if dt >120 :
            result = {'message': 'کد معتبر نیست'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = models.Auth.objects.get(mobile=mobile)
        except models.Auth.DoesNotExist:
            return Response({'message': 'کاربری با این شماره همراه وجود ندارد'}, status=status.HTTP_404_NOT_FOUND)
        
        
        otp_obj.delete()
        token = fun.encryptionUser(user)

        return Response({

            'access': token,
        }, status=status.HTTP_200_OK)
    
    

# Sign up
class AuthCreateView(generics.CreateAPIView):
    queryset = models.Auth.objects.all()
    serializer_class = serializers.AuthSerializer

    def post(self, request):
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        user = models.Auth.objects.filter(mobile=mobile ).first()
        otp_code = models.Otp.objects.filter(mobile=mobile).first()
        if str(code) != str(otp_code.code) :
            return Response({'message': 'کد نادرست است'}, status=status.HTTP_400_BAD_REQUEST)
        if user :
            return Response({'message': 'شماره موبایل موجود است'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Consultant
class ConsultantListCreateView(generics.ListCreateAPIView):
    queryset = models.Consultant.objects.all()
    serializer_class = serializers.ConsultantSerializer
    permission_classes = [IsAuthenticated]

# Consultant
class ConsultantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Consultant.objects.all()
    serializer_class = serializers.ConsultantSerializer
    permission_classes = [IsAuthenticated]

# User Profile All
class UserListCreateView(generics.ListCreateAPIView):
    queryset = models.Auth.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# User Profile 
class UserProfileView(APIView):
    def get(self , request):
        Authorization = request.headers['Authorization']
        if not Authorization:
            return Response({'error': 'Authorization header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = fun.decryptionUser(Authorization)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user_instance = user.first()
        serializer = UserSerializer(user_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    






