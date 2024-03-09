from django.urls import path
from .views import CreateAccount, UserDetails, UserLogin

app_name = 'accounts'
urlpatterns = [
    path('signin/', CreateAccount.as_view(), name='create'),
    path('<slug:slug>/', UserDetails.as_view(), name='details'),
    path('login/', UserLogin.as_view(template_name='login.html'), name='login_view'),

]