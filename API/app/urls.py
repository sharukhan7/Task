from allauth.account.views import confirm_email
from django.urls import path , include
from django.conf.urls import url
from . import views
from .views import *
import urllib


urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    #email confirmation with register and login , logout 
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
   
    #Income
    path('list/income/',views.ListIncome.as_view()),
    path('create/income/',views.CreateIncome.as_view()),

    path('list/income/<int:pk>/',views.ListIncome.as_view()),
    path('update/income/<int:pk>/',views.UpdateIncome.as_view()),
    path('delete/income/<int:pk>/',views.DeleteIncome.as_view()),

    #Expense
    path('list/expense/',views.ListExpense.as_view()),
    path('create/expense/',views.CreateExpense.as_view()),

    path('list/expense/<int:pk>/',views.ListExpense.as_view()),
    path('update/expense/<int:pk>/',views.UpdateExpense.as_view()),
    path('delete/expense/<int:pk>/',views.DeleteExpense.as_view()),

    #income catecory
    path('list/categories/',views.ListCategory.as_view()),
    path('create/categories/',views.CreateCategory.as_view()),

    path('list/categories/<int:pk>/',views.ListCategory.as_view()),
    path('update/categories/<int:pk>/',views.UpdateCategory.as_view()),
    path('delete/categories/<int:pk>/',views.DeleteCategory.as_view()),

    #expense type
    path('list/type/',views.ListExpensetype.as_view()),
    path('create/type/',views.CreateExpensetype.as_view()),

    path('list/type/<int:pk>/',views.ListExpensetype.as_view()),
    path('update/type/<int:pk>/',views.UpdateExpensetype.as_view()),
    path('delete/type/<int:pk>/',views.DeleteExpensetype.as_view()),
    

    #analysis
    path('analysis/<int:year>/<int:month>/', views.AnalyticsView.monthly, name="monthly"),

]


