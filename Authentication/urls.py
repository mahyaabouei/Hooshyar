from django.urls import path
from .views import CaptchaViewset , OtpViewset , LoginViewset ,UserProfileView, ConsultantListCreateView ,ConsultantDetailView , AuthCreateView , UserListCreateView

urlpatterns = [
    path('captcha/', CaptchaViewset.as_view(), name='captcha'),
    path('otp/', OtpViewset.as_view(), name='otp'),
    path('login/', LoginViewset.as_view(), name='login'),
    path('signup/',AuthCreateView.as_view(), name='signup'),
    path('userprofile/', UserListCreateView.as_view(), name='userprofile'),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('consultant/', ConsultantListCreateView.as_view(), name='consultant'),
    path('consultant/<int:pk>/',ConsultantDetailView.as_view(), name='consultant'),
    
    ]