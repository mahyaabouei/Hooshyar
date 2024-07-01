from django.urls import path
from .views import PayViewset 

urlpatterns = [
    path('perpay/', PayViewset.as_view(), name='perpay'),

]