from django.shortcuts import render, redirect
from .forms import DiaryForm, CommentForm
from .models import DiaryArticle, Comments
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import random

# Create your views here.

@login_required
def index(request):
    recent_articles = DiaryArticle.objects.filter(created_date__gte=datetime.now()-timedelta(days=7)) # 최근 7일 간의 게시물만 포함
    random_articles = []
    length = 4
    
    if len(recent_articles) >= length:
        rand_article = random.sample(list(recent_articles), length)
        for article in rand_article:
            random_articles.append(article)
    else:
        random_articles = False
                
    context = {
        'random_articles': random_articles,
    }
    return render(request, 'articles/index.html', context)
    
@login_required
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

@login_required
def detail(request, article_id):
    diary_article = DiaryArticle.objects.get(id=article_id)
    comments = diary_article.comments_set.all()
    comment_form = CommentForm()
    diary_article.hits += 1
    
    # try:
    context = {
    'diary_article': diary_article,
    'form': comment_form,
    'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
    
    # except:
    #     comments = False
    #     context = {
    #         'diary_article': diary_article,
    #         'form': comment_form,
    #         'comments': comments,
    #     }
    #     return render(request, 'articles/detail.html', context)