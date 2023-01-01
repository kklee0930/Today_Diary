from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    context = {
        
    }
    return render(request, 'accounts/login.html', context)