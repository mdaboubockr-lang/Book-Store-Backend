from django.contrib.postgres import serializers

from store_APIS.models import Book
from rest_framework import serializers
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_2 = serializers.CharField(
        write_only=True, 
        min_length=8, 
        label="Confirm Password"
    )
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password_2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError({
                "password_2": "Passwords do not match. Please try again."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_2')
        user = User.objects.create_user(**validated_data)
        return user
