from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Car, Photo
from .serializers import CarSerializer, PhotoSerializer

from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def register(request):
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car = serializer.save(user = request.user)
            photo_serializer = PhotoSerializer(data=request.data["photos"], many=True)
            if photo_serializer.is_valid(raise_exception=True):
                photo_serializer.save(car=car)
            # serializer.save(photos=request.data.images, many=True)
            return Response(serializer.data)
        return Response(serializer.data)

