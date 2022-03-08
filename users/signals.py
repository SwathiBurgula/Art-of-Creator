from django.db.models.signals import post_save,post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


def createProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            name = user.first_name,
            username = user.username,
            email = user.email,
            # profile_image = '/profiles/user-default.png'
        )
        print('Same Record created in Profile ')

        subject = "Welcome to our website"
        message = "We glad you are here"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )