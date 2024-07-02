from django.urls import path
from .views import PayViewset 

urlpatterns = [
    path('perpay/<int:kind>/', PayViewset.as_view(), name='perpay'),

]