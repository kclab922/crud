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

8. 앱 생성
```
django-admin startapp <app-name>
```

9. 앱 등록 =>`settings.py`
```
INSTALLED_APPS = [
    ...
    `<app-name>`,
]
    
```