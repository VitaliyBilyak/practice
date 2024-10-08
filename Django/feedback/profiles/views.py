from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView


from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfileView(ListView):
    model = UserProfile
    template_name = "user_profiles.html"
    context_object_name = "profiles"