from django.urls import path
from . import views
from .views import your_view

urlpatterns = [
    path('', views.CompanyView.as_view()),
    path('<slug:slug>/', views.CompanyDetailView.as_view(), name='companysingle'),
    path('her', your_view)
]