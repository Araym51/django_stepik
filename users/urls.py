from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import login, logout, UserRegistrationView, UserProfileView  # registration, profile,

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    # path('register/', registration, name='register'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    # path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
