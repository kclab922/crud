from django.shortcuts import render, redirect
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


def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    # return redirect('/index/')
    return redirect(f'/posts/{post.id}/')


def delete(request, id):
    # 내가 지우고 싶은 게시물 찾기
    post = Post.objects.get(id=id)
    # delete 메소드 호출
    post.delete()

    return redirect('/index/')

def edit(request, id):
    # 일단 기존 정보 찾아오기 (read와 똑같음)
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'edit.html', context)


def update(request, id):
    # 방금 사용자가 수정한 데이터 가져오기 (edit.html input box에 넣었을 것)
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 기존 데이터 가져오기
    post = Post.objects.get(id=id)

    # 기존 데이터의 객체인 post를 가져와서 수정된 데이터로 바꿔주기
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')