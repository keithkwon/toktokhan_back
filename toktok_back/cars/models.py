import uuid
import os
from django.db import models
from django.conf import settings

# 유니크한 파일명을 갖기위한 함수
def image_file_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('images/', filename)

# Create your models here.
class Car(models.Model):
    maker = models.CharField(max_length=255)
    accident= models.IntegerField()
    # blank=true가 필요할수도 있음. 
    accident_details = models.CharField(max_length=255, null=True, blank=True)
    price_suggestion = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.maker

class Photo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to=image_file_path, null=False)