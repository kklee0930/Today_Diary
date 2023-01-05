from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('creatediary/', views.create_diary, name='create_diary'),
    # path('<int:pk>', views.detail, name='detail'),
    
]
