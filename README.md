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