from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SurveyViewSet

app_name = 'mainapp'
router = DefaultRouter()
router.register('survey', SurveyViewSet)

urlpatterns = [
    path('/api/admin/', include(router.urls)),
]