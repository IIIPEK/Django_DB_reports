from django.shortcuts import render, redirect


# Create your views here.

def logout(request):
    logout(request)
    return redirect('main:index')

def profile(request):
    return render(request, 'users/profile.html')