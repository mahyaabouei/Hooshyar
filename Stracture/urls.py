from django.urls import path
from .views import SelectTimeViewset ,SetTimeConsultant

urlpatterns = [
    path('selecttime/<int:pk>/', SelectTimeViewset.as_view(), name='select-time'),
    path('settime/consultant/', SetTimeConsultant.as_view(), name='set-time-consultant'),

]


