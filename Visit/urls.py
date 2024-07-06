from django.urls import path
from .views import  VisitViewset , QuestionViewset , KindOfCounselingViewset ,VisitConsultationsViewset ,VisitConsultationsDetialViewset 
urlpatterns = [
    path('visit/',VisitViewset.as_view(), name='visit'),
    path('question/',QuestionViewset.as_view(), name='question'),
    path('kindofcounseling/',KindOfCounselingViewset.as_view(), name='kindofcounseling'),
    path('visit/consultations/list/',VisitConsultationsViewset.as_view(), name='visit-consultations-list'),
    path('visit/consultations/<int:id>/',VisitConsultationsDetialViewset.as_view(), name='visit-consultations-detail'),

]


