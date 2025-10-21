from django.urls import path    
from .views import LeaveRequestView 


urlpatterns = [
    path('', LeaveRequestView.as_view(), name='leave-request'),
]