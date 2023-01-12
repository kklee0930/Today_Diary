from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('creatediary/', views.create_diary, name='create_diary'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    
]
