from django.urls import path ,include
from .views import UserLoginApi

app_name= 'user'


urlpatterns = [
    path('login', UserLoginApi.as_view(), name='login'),
]