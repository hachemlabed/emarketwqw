from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    class meta:
        model = Product
        fields = ('name','price')
        
class FullProductSerializer(serializers.Serializer):
    class meta:
        model = Product
        fields = "__all__"
        
        
        