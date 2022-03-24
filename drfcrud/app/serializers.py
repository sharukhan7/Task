from django.db.models import fields
from rest_framework import serializers
from .models import Shopdata
  

class Serializedata(serializers.ModelSerializer):
    class Meta:
        model = Shopdata
        fields = '__all__'
