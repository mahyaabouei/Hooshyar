from django.urls import path
from .views import CaptchaViewset , OtpViewset , LoginViewset ,UserProfileViewset, ConsultantViewset , AuthCreateView ,OtpConsultant ,LoginConsultant,ConsultantProfileViewset

urlpatterns = [
    path('captcha/', CaptchaViewset.as_view(), name='captcha'),
    path('otp/', OtpViewset.as_view(), name='otp'),
    path('otp/consultant/', OtpConsultant.as_view(), name='otp-consultant'),
    path('login/', LoginViewset.as_view(), name='login'),
    path('login/consultant/', LoginConsultant.as_view(), name='login'),
    path('signup/',AuthCreateView.as_view(), name='signup'),
    path('user/profile/', UserProfileViewset.as_view(), name='user-profile'),
    path('consultant/', ConsultantViewset.as_view(), name='consultant'),
    path('consultant/profile', ConsultantProfileViewset.as_view(), name='consultant-profile'),
    
    ]