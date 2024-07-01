from django.urls import path
from .views import PayViewset 

urlpatterns = [
    path('perpay/<int:kind>/<str:code>/', PayViewset.as_view(), name='perpay'),

]