from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
   path('login/', login, name='login'),  # ../users/login/
   path('register/', register, name='register'),
   path('profile/', profile, name='profile'),
   path('logout/', logout, name='logout')
]