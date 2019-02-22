from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from multifile_upload import views

urlpatterns = [
    path('files/', views.PhotoViewSet),
]

urlpatterns = format_suffix_patterns(urlpatterns)
