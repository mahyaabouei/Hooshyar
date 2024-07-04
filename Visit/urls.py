from django.urls import path
from .views import  VisitViewset , QuestionViewset , KindOfCounselingViewset ,VisitConsultations  
urlpatterns = [
    path('visit/',VisitViewset.as_view(), name='visit'),
    path('question/',QuestionViewset.as_view(), name='question'),
    path('kindofcounseling/',KindOfCounselingViewset.as_view(), name='kindofcounseling'),
    path('visit/consultations/',VisitConsultations.as_view(), name='visit-consultations-list'),

]


