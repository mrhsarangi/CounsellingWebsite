from django.urls import path
from .views import CreateAccount, UserDetails, UserLogin

app_name = 'accounts'
urlpatterns = [
    path('signin/', CreateAccount.as_view(), name='signin'),
    path('<slug:slug>/', UserDetails.as_view(), name='details'),
    path('user/login/', UserLogin.as_view(), name='login_view'),

]