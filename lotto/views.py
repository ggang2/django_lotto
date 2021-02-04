from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers # models.py에서 DB table 설정 가져오기
from .forms import PostForm # forms.py에서 form 형식 불러오기

# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Hello, world!</h1>')

def index(request):

    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos}) #index.html이 더 일반,


def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello, world!</h1>') #emmet 자동 완성


def post(request):
    #처음 홈페이지 도착은 GET #버튼을 누른 뒤에는 POST

    if request.method == "POST" : #포스트 요청이면
        form = PostForm(request.POST)

        if form.is_valid(): #유저가 제출한 데이터가 조건을 충족하는지 봐준다(models.py에 내건 조건)
            lotto = form.save(commit = False)
            #DB 반영을 미루고 임시로 저장한다(name, text뿐이기에) => DB 안 하나의 행
            lotto.generate()

            return redirect('lotto') #urls에서 먹여둔 이름

    else: #포스트 요청이 아니면, 빈 상태로 만들어준다
        form = PostForm() #empty form
        return render(request, 'lotto/form.html', {'form':form}) #보통 dict 안에서는 변수명과 맞춰주는 편


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey) #pk = data 순서
    return render(request, 'lotto/detail.html', {'lotto':lotto})
