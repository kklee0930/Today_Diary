from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'articles/index.html', context)
    
# def detail(request, pk):
#     context = {
        
#     }
#     return render(request, 'articles/', context)