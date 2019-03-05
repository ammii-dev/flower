from django.urls import path, include
from rest_framework.routers import DefaultRouter

from escort import views


router = DefaultRouter()
router.register('', views.EscortsViewSet)
router.register('post', views.PostEscortsViewSet)
router.register('edit', views.EditEscortViewSet)
router.register('profile', views.EscortViewSet)


app_name = 'escort-posts'

urlpatterns = [
    path('', include(router.urls))
]
