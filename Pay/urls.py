from django.urls import path
from .views import DiscountListCreateView , DiscountDetailView

urlpatterns = [
    path('discount/', DiscountListCreateView.as_view(), name='discount'),
    path('discount/<int:pk>/',DiscountDetailView.as_view(), name='discount')

]