# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile, ProfilePhotos, ProfileLibrary, FriendRequest
# ProfileUserPhoto, ProfileUserPost

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
# admin.site.register(ProfilePhotoLibrary)
# admin.site.register(ProfileUserPost)
# admin.site.register(ProfileUserPhoto)

admin.site.register(ProfilePhotos)
admin.site.register(ProfileLibrary)
admin.site.register(FriendRequest)