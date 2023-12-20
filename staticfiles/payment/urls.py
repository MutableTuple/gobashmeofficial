from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views

urlpatterns = [
    path('<str:username>/', views.Payment, name='payment'),
    path('main/charge/', views.charge, name='charge'),
    path('success/<str:args>', views.successMessage, name='success'),
]
