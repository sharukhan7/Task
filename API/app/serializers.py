from django.db.models import fields
from rest_framework import serializers
from .models import Incomemodel,Expensemodel,Categories,Expensetype
  
class Serialize_incomemodel(serializers.ModelSerializer):
    class Meta:
        model = Incomemodel
        fields = '__all__'

class Serialize_expensemodel(serializers.ModelSerializer):
    class Meta:
        model = Expensemodel
        fields = '__all__'

class Serialize_category(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class Serialize_expensetype(serializers.ModelSerializer):
    class Meta:
        model = Expensetype
        fields = '__all__'

