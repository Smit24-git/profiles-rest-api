from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profile_api import views

# required for viewset urls only
router = DefaultRouter()
router.register('hello-viewset',
                views.HelloViewSet,
                base_name = 'hello-viewset')
router.register('profile',views.UserProfileViewSet)
#base_name is not required if you have queryset on views.
#base_name will be overwritten by queryset
urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
