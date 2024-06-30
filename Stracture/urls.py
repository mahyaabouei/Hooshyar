from django.urls import path
from .views import SelectTimeViewset 

urlpatterns = [
    path('selecttime/', SelectTimeViewset.as_view(), name='selecttime'),

]


