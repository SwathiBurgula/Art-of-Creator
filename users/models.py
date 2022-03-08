from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    # name= models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

    def __str__(self): 
        return str(self.user.username)
