import uuid
import os
from django.db import models
from django.conf import settings

# 유니크한 파일명을 갖기위한 함수
# 갈아엎으면서 필요없어짐
# def image_file_path(instance, filename):
#     extension = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{ext}'
#     return os.path.join('images/', filename)

# Create your models here.
class Car(models.Model):
    maker = models.CharField(max_length=255)
    imported = models.BooleanField()
    accident= models.BooleanField()
    accident_details = models.CharField(max_length=255, null=True, blank=True)
    price_suggestion = models.IntegerField()
    temporary = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.maker

class Photo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=255)