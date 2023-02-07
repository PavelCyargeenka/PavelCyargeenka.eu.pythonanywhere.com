from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('success/', views.Success.as_view()),
]