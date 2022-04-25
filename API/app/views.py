from django.shortcuts import render
from django.db.models import Sum, Count
import datetime

from django.views import generic
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Categories,Incomemodel,Expensetype,Expensemodel


#List
class ListIncome(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel
class ListExpense(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensemodel.objects.all()
    serializer_class = Serialize_expensemodel
class ListCategory(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category
class ListExpensetype(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

#Create
class CreateIncome(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel
class CreateExpense(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensemodel
class CreateCategory(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category
class CreateExpensetype(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

#Update
class UpdateCategory(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category

class UpdateExpensetype(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

class UpdateIncome(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel

class UpdateExpense(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensemodel.objects.all()
    serializer_class = Serialize_expensemodel

#delete
class DeleteCategory(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = Serialize_category

class DeleteExpensetype(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensetype.objects.all()
    serializer_class = Serialize_expensetype

class DeleteIncome(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Incomemodel.objects.all()
    serializer_class = Serialize_incomemodel

class DeleteExpense(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Expensemodel.objects.all()
    serializer_class = Serialize_expensemodel

#analysis
def validate(date_text):
    try:
        d=datetime.datetime.strptime(date_text, '%Y-%m')
        print(str(d).split('-'))
        l= str(d).split('-')
        return l[0:2]
    except:
        return False
#Expense by month
@api_view(['GET'])
def ListTotalExpense(request):
    if request.query_params:
        if validate(request.query_params['date']):
            yy,dd=validate(request.query_params['date'])
            items = Expensemodel.objects.filter(date__month=dd,date__year=yy )
            total = items.aggregate(sum=Sum('expense'))
        else:
            return Response({'Incorrect date format, should be YY-MM '})
    else:
        items = Expensemodel.objects.all( )
    
    if items:
        data = Serialize_expensemodel(items ,  many=True).data
        if request.query_params:
            return Response({'Sum of total expense':total})
        else:
            return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    

#income by month
@api_view(['GET'])
def ListTotalIncome(request):
    if request.query_params:
        if validate(request.query_params['date']):
            yy,dd=validate(request.query_params['date'])
            items = Incomemodel.objects.filter(date__month=dd,date__year=yy )
            total = items.aggregate(sum=Sum('monthly_income'))
            
        else:
            return Response({'Incorrect date format, should be YY-MM '})
    else:
        items = Incomemodel.objects.all( )
    
    if items:
        data = Serialize_incomemodel(items ,  many=True).data
        if request.query_params:
            return Response({'Sum of total Income':total})
        else:
            return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    