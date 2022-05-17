from attr import field
from rest_framework import serializers
from .models import corporate,user
class corporateSerializer(serializers.ModelSerializer):
    class Meta:
        model = corporate
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
