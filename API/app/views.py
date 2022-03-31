from django.shortcuts import render
from django.db.models import Sum, Count

from django.views import generic
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Categories,Incomemodel,Expensetype,Expensemodel

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)   
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


#List
class ListIncome(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel
class ListExpense(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    #queryset = Expensemodel.objects.all()
    queryset = Expensemodel.objects.filter(date__year='2022', date__month='03')
    serializer_class = Serialize_expensemodel
class ListCategory(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category
class ListExpensetype(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

#Create
class CreateIncome(generics.CreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel
class CreateExpense(generics.CreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensemodel
class CreateCategory(generics.CreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category
class CreateExpensetype(generics.CreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

#Update
class UpdateCategory(generics.RetrieveUpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category

class UpdateExpensetype(generics.RetrieveUpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

class UpdateIncome(generics.RetrieveUpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel

class UpdateExpense(generics.RetrieveUpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Expensemodel.objects.all()
    serializer_class = Serialize_expensemodel

#delete
class DeleteCategory(generics.RetrieveDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category

class DeleteExpensetype(generics.RetrieveDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

class DeleteIncome(generics.RetrieveDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel

class DeleteExpense(generics.RetrieveDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Expensemodel.objects.all()
    serializer_class = Serialize_expensemodel

#analysis
class AnalyticsView(generic.ListView):
    
    def monthly(request, year, month):
        print('test printing')
        # get user expense objects
        exp = Expensemodel.objects.filter(created_by=request)
        print('test printing after')
        print(exp)
        ser = Serialize_expensemodel(exp)
        content = {ser}
        return Response(ser)