# CRUD

- create read update delete

## 프로젝트 구조 작성

1. 프로젝트 폴더 생성
2. 프로젝트 폴더를 vscode로 열기
    - `.gitignore`, `README.md` 만들기 (추후 돌이키기 어려우므로 미리 생성)
3. django 프로젝트 생성
```
django-admin startproject <pjt-name> .
```

4. 가상환경 설정(생성)
```
python -m venv venv 
# 파이썬 실행 / module 사용할게 / venv: 가상환경 virtual environment / 내가 만들려는 폴더명
```

5. 가상환경 활성화 
    - `venv`가 터미널에 출력 되었는지 확인
```
source venv/Scripts/activate
```

6. 가상환경에 django 설치
```
pip install django
```

7. 서버 실행 확인
```
python manage.py runserver
```
`ctrl+c`로 나오기

8. 앱 생성
```
django-admin startapp <app-name>
```

9. 앱 등록 => `<pjt-name>폴더`=> `settings.py`
```
INSTALLED_APPS = [
    ...
    `<app-name>`,
]
```

10. `urls.py` => `views.py` => `templates/*.html`



## Model

1. 모델 정의 (`model.py`)  
    - 모델명은 기본적으로 단수

```python
class Post(models.Model):
    # Charfield 는 TextField에 비해 짦은 내용
    title = models.CharField(max_length=100)
    content = models.TextField()
```

2. 번역본 생성
    - 파이썬 세상에서 SQL 세상으로 이주시키기 위한 준비로 번역본 생성
```
python manage.py makemigrations
```

3. DB에 반영
    - 이주시켜!
    - 내가 만든 posts가 제대로 포함되어있는지가 중요. 
    - 길게 나오는 이유는 장고에 내장된 애들이 같이 이주되어서.
```
python manage.py migrate
```

4. 생성한 모델을 admin에 등록
```python
from django.contrib import admin
from .models import Post
     # . => 현재 나와 같은 폴더 내에 있다는 의미

# Register your models here.

admin.site.register(Post)
```

5. 관리자 계정 생성
```
python manage.py createsuperuser
```


## CRUD
> Create, Read, Update, Delete

### 1. Read
    - 데이터베이스에 있는 게시물을 읽는 것

- 전체 게시물 출력 (`models.py`)
```python
def index(request):
    # Post라는 클래스 안의 objects에 접근해서 all이라는 메소드 실행
    posts = Post.objects.all()
    
    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)
```

- 하나의 게시물 출력
```python
def detail(request, id):
    # Post라는 전체데이터에서 get(가져와) 
    # post는 하나의 게시물이므로 단수. 
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)
```


### 2. Create
- 사용자에게 데이터 받고, 저장


### 3. Delete