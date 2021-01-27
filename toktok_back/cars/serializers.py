from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Car, Photo

class CarSerializer(serializers.ModelSerializer)