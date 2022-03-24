from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact),
    path('employee/', views.employee_list),
    path('employee/<int:pk>/', views.employee_detail),
]