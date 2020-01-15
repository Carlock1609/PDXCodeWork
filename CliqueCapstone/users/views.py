from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth.decorators import login_required # Decorators
from .models import CustomUser, UserProfile
# from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms

from .forms import CustomUserCreationForm, ProfileUpdateForm

from django.contrib.auth import authenticate, login # More authentication
from django.contrib import messages

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
@login_required
def profile_page(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(request.POST, instance=request.user.user)
    user_id = request.user.id
    context = {
        'p_form': p_form,
        'user_profile': UserProfile.objects.get(user_id=user_id),
    }
    return render(request, 'users/profile.html', context)




# def edit_user(request, pk):
#     user = CustomUser.objects.get(pk=pk)
#     user_form = UserProfileForm(instance=user)
 
#     ProfileInlineFormset = inlineformset_factory(CustomUser, UserProfile, fields=('first_name', 'social_media', 'follower_amount', 'experience', 'portfolio_links', 'bio', 'city', 'country', 'friends',))
#     formset = ProfileInlineFormset(instance=user)
 
#     if request.user.is_authenticated() and request.user.id == user.id:
#         if request.method == "POST":
#             user_form = UserProfileForm(request.POST, request.FILES, instance=user)
#             formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
#             if user_form.is_valid():
#                 created_user = user_form.save(commit=False)
#                 formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
#                 if formset.is_valid():
#                     created_user.save()
#                     formset.save()
#                     return HttpResponseRedirect('/accounts/profile/')
 
#         return render(request, "account/account_update.html", {
#             "noodle": pk,
#             "noodle_form": user_form,
#             "formset": formset,
#         })
#     else:
#         raise PermissionDenied