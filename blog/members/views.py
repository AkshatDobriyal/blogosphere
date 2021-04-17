from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditUserSettingsForm, PasswordChangingForm
from myblog.models import Profile
# Create your views here.

class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserSettingsEditView(generic.UpdateView):
    form_class = EditUserSettingsForm
    template_name = 'registration/edit_user_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')
    #success_url = reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        context['page_user'] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ('bio', 'profile_pic', 'linkedin_url', 'facebook_url', 'instagram_url')
    success_url = reverse_lazy('home')






