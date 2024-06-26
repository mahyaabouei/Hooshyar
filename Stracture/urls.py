from django.urls import path
from .views import SelectTimeDetailView , SelectTimeListCreateView

urlpatterns = [
    path('selecttime/', SelectTimeListCreateView.as_view(), name='selecttime'),
    path('selecttime/<int:pk>/',SelectTimeDetailView.as_view(), name='selecttime')

]


