from django.urls import path
from django.shortcuts import render
from accounts.views import SignUpView


app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]