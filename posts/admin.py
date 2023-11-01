from django.contrib import admin
from .models import Post
     # . => 현재 나와 같은 폴더 내에 있다는 의미

# Register your models here.

admin.site.register(Post)