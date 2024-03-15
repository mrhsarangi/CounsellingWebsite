from django.urls import path
from .views import CreateAccount, CreateAccountCounselor, UserDetails, UserLogin, LogoutView, PasswordChangeView, PasswordResetView, UserUpdate, UserDelete

app_name = 'accounts'
urlpatterns = [
    path('<slug:slug>/', UserDetails.as_view(), name='details'),
    path('students/sign-up/', CreateAccount.as_view(), name='students-signup'),
    path('counselors/sign-up/', CreateAccountCounselor.as_view(), name='counselor-signup'),
    path('user-actions/log-in/', UserLogin.as_view(), name='login'),
    path('user-actions/log-out/', LogoutView.as_view(), name='logout'),
    path('<slug:slug>/update/', UserUpdate.as_view(), name='update'),
    path('<slug:slug>/delete-account/', UserDelete.as_view(), name='delete'),


]