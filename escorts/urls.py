from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from escorts import views

urlpatterns = [
    path('escorts/', views.escort_list),
    path('escorts/<int:pk>', views.escort_detail),
    path('escorts/create/', views.create_escort),
    path('escorts/edit/<int:pk>', views.edit_escort),
]

urlpatterns = format_suffix_patterns(urlpatterns)
