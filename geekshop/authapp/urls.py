from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
from authapp.views import login, register, logout, profile
=======
from authapp.views import login, register, logout
>>>>>>> Lesson_6

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
<<<<<<< HEAD
    path('profile/', profile, name='profile'),
=======
>>>>>>> Lesson_6
    path('logout/', logout, name='logout')]
