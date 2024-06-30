from django.urls import path
from .views import SelectTimeViewset 

urlpatterns = [
    path('selecttime/<int:pk>/', SelectTimeViewset.as_view(), name='selecttime'),

]


