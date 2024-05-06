from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models

User = get_user_model() 
class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['email','username','password','confirm_password']
        extra_kwargs = {
            'email' :{'required':True,'allow_blank':False},
            'username' :{'required':True,'allow_blank':False},
            'password' :{'required':True,'allow_blank':False,'min_length':8},
        }
    
def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("The passwords do not match.")
        return data

def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        return create(validated_data) 