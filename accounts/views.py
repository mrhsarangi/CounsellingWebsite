from .models import User
from .forms import  UserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth import get_user
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CreateAccount(CreateView):

    model = User
    form_class = UserForm
    success_url = reverse_lazy(viewname='login_view')

    def form_valid(self, form) :

        user_object = form.save(commit=False)
        user_object.username = user_object.email.split('@')[0]
        user_object.slug = user_object.username
        return super().form_valid(form)
    

class UserDetails( DetailView):
    
    model = User
    template_name = 'user_detail.html'


class UserLogin(LoginView):


    template_name = 'login.html'
    

    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    