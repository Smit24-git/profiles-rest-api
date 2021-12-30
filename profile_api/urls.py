from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profile_api import views

# required for viewset urls only
router = DefaultRouter()
router.register('hello-viewset',
                views.HelloViewSet,
                base_name = 'hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
