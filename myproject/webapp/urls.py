from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import employeelist

urlpatterns = [
    path('employees/', employeelist.as_view(), name='employees'),
]
