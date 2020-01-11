from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save

# creating inbox instance when created aswell
# FIGURE OUT WHY THIS CAUSES AN IMPORTING ERROR. 
# from inboxApp.models import InboxDB

# Create your models here.
class CustomUser(AbstractUser):
    pass
# ADD ADDITIONAL FIELDS HERE

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user', on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=20,) # REQUIRED
    social_media = models.URLField(default='', blank=True, null=True) # REQUIRED
    follower_amount = models.IntegerField(default=0, blank=True, null=True) # REQUIRED
    experience = models.TextField(max_length=500, default='', blank=True, null=True) # REQUIRED

    portfolio_links = models.URLField(default='', blank=True, null=True)
    bio = models.TextField(max_length=500, default='', blank=True, null=True)
    city = models.CharField(max_length=20, default='', blank=True, null=True)
    country = models.CharField(max_length=20, default='', blank=True, null=True)
    cliques = models.IntegerField(default=0, blank=True, null=True) # CALL IT CLIQUES

    profile_pic = models.ImageField(upload_to='images/') # FIGURE OUT PILLOW FROM LIBRARY LAB
    photo_library = models.ImageField()

    def __str__(self):
        return f"{self.user.username}'s Profile"

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        
        # FIGURE OUT WHY THIS CAUSES AN IMPORTING ERROR. 
        # user_inbox = InboxDB.objects.create(users_inbox=kwargs['instance'])
        
post_save.connect(create_profile, sender=CustomUser)

# class UserImage(models.Model):
#     user_image = models.ImageField(upload_to='images/')
    