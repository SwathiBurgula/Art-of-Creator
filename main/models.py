# from django.db import models
# from email.policy import default
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify

# # Create your models here.

# class mainPost(models.Model):
#     image = models.ImageField(upload_to='photos/',null=True ,blank=True, default='website.jpg')
#     title= models.CharField(max_length=300, unique=True)
#     likes= models.IntegerField(default=0)
#     dislikes= models.IntegerField(default=0)

#     def save(self, *args, **kwargs):
#         self.url= slugify(self.title)
#         super(mainPost, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.title


# class mainPreference(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE)
#     post= models.ForeignKey(mainPost, on_delete=models.CASCADE)
#     value= models.IntegerField()
#     date= models.DateTimeField(auto_now= True)

    
#     def __str__(self):
#         return str(self.user) + ':' + str(self.post) +':' + str(self.value)

#     class Meta:
#        unique_together = ("user", "post", "value")
