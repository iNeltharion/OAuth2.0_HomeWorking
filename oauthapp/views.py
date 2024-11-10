from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html', {'user': request.user})

def index(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def index(request):
    return render(request, 'index.html', {'user': request.user})
