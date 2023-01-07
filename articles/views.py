from django.shortcuts import render, redirect
from .forms import DiaryForm
from .models import DiaryArticle
from datetime import datetime, timedelta
import random

# Create your views here.
def index(request):
    recent_articles = DiaryArticle.objects.filter(created_date__gte=datetime.now()-timedelta(days=3)) # 최근 3일 간의 게시물만 포함
    random_articles = []
    while True:
        if len(random_articles) >= 4:
            break
        rand_article = random.choice(recent_articles)
        if rand_article not in random_articles:
            random_articles.append(rand_article)
            
    context = {
        'random_articles': random_articles,
    }
    return render(request, 'articles/index.html', context)
    
def create_diary(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        
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