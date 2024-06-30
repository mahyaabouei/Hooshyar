from django.urls import path
from .views import CaptchaViewset , OtpViewset , LoginViewset ,UserProfileView, ConsultantViewset , AuthCreateView , UserListCreateView

urlpatterns = [
    path('captcha/', CaptchaViewset.as_view(), name='captcha'),
    path('otp/', OtpViewset.as_view(), name='otp'),
    path('login/', LoginViewset.as_view(), name='login'),
    path('signup/',AuthCreateView.as_view(), name='signup'),
    path('userprofile/', UserListCreateView.as_view(), name='userprofile'),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('consultant/', ConsultantViewset.as_view(), name='consultant'),
    
    ]