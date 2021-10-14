from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp.views import SurveyViewSet, QuestionViewSet, SurveyUserView, SurveyDetailView, AnswerSurvey, \
    ResultAnswerView

router = DefaultRouter()
router.register('survey', SurveyViewSet)
router.register('question', QuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', include(router.urls)),
    path('api/survey/', SurveyUserView.as_view()),
    path('api/survey/<int:pk>/', SurveyDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/answer/<int:pk>/', AnswerSurvey.as_view()),
    path('api/result_answer/<int:id_user>/', ResultAnswerView.as_view()),
]


