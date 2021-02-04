from django.contrib import admin
from .models import GuessNumbers #만든 함수 불러오기 #.models = lotto.models #현재 위치한 폴더에서 불러오기는 .을 쓴다

# Register your models here.

admin.site.register(GuessNumbers)
