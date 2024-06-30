from django.urls import path
from .views import  VisitViewset , QuestionViewset , KindOfCounselingViewset 
urlpatterns = [
    path('visit/',VisitViewset.as_view(), name='visit'),
    path('question/',QuestionViewset.as_view(), name='question'),
    path('kindofcounseling/',KindOfCounselingViewset.as_view(), name='kindofcounseling'),

]


