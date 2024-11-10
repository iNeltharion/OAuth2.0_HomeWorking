from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/google/', include('social_django.urls', namespace='social')),
    path('auth/complete/', include('social_django.urls')),
]
