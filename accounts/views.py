from django.forms import BaseModelForm
from django.http import HttpResponse
from .models import User
from .forms import  UserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CreateAccount(CreateView):

    model = User
    form_class = UserForm
    success_url = reverse_lazy(viewname='accounts:login')

    def form_valid(self, form) :

        user_object = form.save(commit=False)
        user_object.username = user_object.email.split('@')[0]
        user_object.slug = user_object.username
        return super().form_valid(form)
    

class UserDetails(LoginRequiredMixin, DetailView):
    
    model = User


class UserLogin(LoginView):


    template_name = 'login.html'
    

    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    

class UserUpdate(LoginRequiredMixin, UpdateView):

    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = "accounts/user_form.html" 
    success_url = reverse_lazy(viewname='homepage')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        
        user_object = form.save(commit=False)
        user_object.username = user_object.email.split('@')[0]
        user_object.slug = user_object.username
        return super().form_valid(form)

    