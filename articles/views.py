from django.shortcuts import render, redirect
from .forms import DiaryForm
from .models import DiaryArticle
# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'articles/index.html', context)
    
def create_diary(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('articles:index')
        
    else:
        form = DiaryForm()
            
    context = {
        'form': form,
    }
    
    return render(request, 'articles/creatediary.html', context) # 이슈 발생시 다시 돌아가기

# def detail(request, pk):
#     context = {
        
#     }
#     return render(request, 'articles/', context)