from django.db import models
from django.contrib.auth.models import AbstractUser
from gesler.settings import MEDIA_URL,STATIC_URL
# Create your models here.
# Implemtenacion del campo image en la tabla usuario 

class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True )

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
