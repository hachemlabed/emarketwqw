from django.shortcuts import get_object_or_404, render
from .models import Product
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import FullProductSerializer,ProductSerializer
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    data = request.data 
    serializer = FullProductSerializer(data=data)
    
    if serializer.is_valid():
        product = Product.objects.create(**data,user=request.user)
        res = FullProductSerializer(product,many=False)
        return Response({'details':'product created succesfully'})
    else : 
        return Response( serializer.errors)
    
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request,pk):
    product = get_object_or_404(Product,id=pk)
    
    if product.user != request.user :
        return Response({"error":"Sorry you can't delete this product"},status = status.HTTP_403_FORBIDDEN)
    else : 
        product.delete()
        return Response({"details":"Delete action is done"}, status = status.HTTP_200_OK)