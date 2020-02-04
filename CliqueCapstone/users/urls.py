from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:id>/', views.profile_page, name='profile'),
    path('update_profile/', views.update_user_profile, name='update_profile'),
    path('profile/upload/delete/<int:id>/', views.delete_image, name='delete'),
    # path('profile/addfriend/<int:id>/', views.add_friend, name='add_friend'),
    path('profile/library/', views.photo_library_page, name='photo_library'),
    path('profile/friends_list/<int:id>/', views.friends_list_page, name='friends_list'),
]