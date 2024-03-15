from django.urls import path
from .views import CreateAccount, UserDetails, UserLogin, LogoutView, PasswordChangeView, PasswordResetView, UserUpdate

app_name = 'accounts'
urlpatterns = [
    path('<slug:slug>/', UserDetails.as_view(), name='details'),
    path('user-actions/sign-up/', CreateAccount.as_view(), name='signup'),
    path('user-actions/log-in/', UserLogin.as_view(), name='login'),
    path('user-actions/log-out/', LogoutView.as_view(), name='logout'),
    # path('user_actions/change_password/', 
    #      PasswordChangeView.as_view(template_name = 'change_password.html',), 
    #      name='change_password'),
    path('<slug:slug>/update/', UserUpdate.as_view(), name='update'),


]