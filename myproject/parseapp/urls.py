from django.urls import path
from .views import parse_pdf, home

urlpatterns = [
    path('', home, name='home'),
    path('parse/', parse_pdf, name='parse_pdf'),
]
