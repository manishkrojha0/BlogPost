from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='user-registration'),
    path('order/',views.newForm.as_view(),name='order')
]