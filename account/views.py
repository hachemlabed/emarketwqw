from urllib import response
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view,permission_classes
from rest_framework.generics import (CreateAPIView,)
from rest_framework.permissions import (AllowAny,IsAuthenticated)
from .serializers import SignupSerializer,validate
from . import models 
from .models import User,UserManager
# Create your views here.
def count_upper(s):
    count = 0
    for c in s :
        if c.isupper():
            count +=1
    return count
 
def  count_number(s):
    count = 0
    for c in s :
        if c.isdigit():
            count +=1
    return count 
        
@api_view(['POST']) 
def create_user(request):
    data = request.data 
    user = SignupSerializer(data = data)
    
    if user.is_valid():
        if not User.objects.filter(username = data['username']).exists():
            if data['password'] != data['confirm_password'] :
                return Response({'details':'the passwords you entered doesnt match !!'},status=status.HTTP_400_BAD_REQUEST)
            if count_upper(data['password']) < 1 or count_number(data['password']) < 1:
                return  Response({'details':'the password you entered doesent have  uppercase or digits  '},status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create(
                email = data['email'],
                password = make_password(data['password']),
                confirm_password = make_password(data['confirm_password']),
                username = data['username']
            )
            
            return Response({'details':'Your account registered succefully'},
                            status = status.HTTP_201_CREATED)
        else :
            return Response({'details':'the email you entered already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
    else : return Response(user.errors)
    
    