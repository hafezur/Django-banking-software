from django.urls import path
from .views import UserRegistrationViews,UserLoginView,UserLogoutView,UserBankAccountUpdateView

urlpatterns=[
    path('register/',UserRegistrationViews.as_view(), name='register'), # for class based view we must use .as_view();
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/',UserLogoutView.as_view(), name='logout'),
    path('profile/',UserBankAccountUpdateView.as_view() ,name='profile'),
]