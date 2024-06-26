from django.urls import path
from .views import CaptchaViewset , OtpViewset , LoginViewset , ConsultantListCreateView ,ConsultantDetailView

urlpatterns = [
    path('captcha/', CaptchaViewset.as_view(), name='captcha'),
    path('otp/', OtpViewset.as_view(), name='otp'),
    path('login/', LoginViewset.as_view(), name='login'),
    path('consultant/',ConsultantListCreateView.as_view(), name='consultant'),
    path('consultant/<int:pk>/',ConsultantDetailView.as_view(), name='consultant'),
    
    ]