from rest_framework import serializers
from rest_framework.views import APIView


class IndexViewSerializer(serializers.Serializer):
    CiscoCustomerName= serializers.CharField()
    class Meta:
        
        fields = ['CiscoCustomerName']


