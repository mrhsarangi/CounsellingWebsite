from django.urls import path
from .views import CreateAccount, AccountDetails

app_name = 'accounts'
urlpatterns = [
    path('signin/', CreateAccount.as_view(), name='create'),
    path('<slug:slug>/', AccountDetails.as_view(), name='details'),
]