from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    # Post라는 클래스 안의 objects에 접근해서 all이라는 메소드 실행
    posts = Post.objects.all()
    
    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)