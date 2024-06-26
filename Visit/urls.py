from django.urls import path
from .views import VisitDetailView , VisitListCreateView , QuestionDetailView , QuestionListCreateView , KindOfCounselingDetailView , KindOfCounselingListCreateView
urlpatterns = [
    path('visit/',VisitListCreateView.as_view(), name='visit'),
    path('visit/<int:pk>/',VisitDetailView.as_view(), name='visit'),
    path('question/',QuestionListCreateView.as_view(), name='question'),
    path('kindofcounseling/',KindOfCounselingListCreateView.as_view(), name='kindofcounseling'),
    path('kindofcounseling/<int:pk>/',KindOfCounselingDetailView.as_view(), name='kindofcounseling')

]


