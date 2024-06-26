from rest_framework import serializers
from . import models  
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Auth
        fields = ['id', 'name', 'last_name', 'national_code', 'phone', 'email']



class OtpSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Otp
        fields = '__all__'




class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consultant
        fields = '__all__'   

