from rest_framework import serializers
from .models import Employee


'''
class employee_serialize(serializers.Serialize):
    name = serializers.CharField()
    gender = serializers.CharField()
    email = serializers.EmailField()



    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

'''

class employee_serialize(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'