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


def detail(request, id):
    # Post라는 전체데이터에서 get(가져와) 
    # post는 하나의 게시물이므로 단수. 
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)