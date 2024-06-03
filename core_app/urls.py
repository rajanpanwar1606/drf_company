from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/company/',CompanyView.as_view(),name = 'company'),
    path('api/v1/company/<int:pk>/',CompanyDetail.as_view(),name = 'by_id'),
]