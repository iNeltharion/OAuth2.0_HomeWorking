from django.urls import path, include
from oauthapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/google/', include('social_django.urls', namespace='social')),
    path('auth/complete/', include('social_django.urls')),
]
