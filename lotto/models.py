from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    # 변수들을 받아줄 DataFrame의 열을 설정한다 => 열 이름과 데이터타입 설정
    name = models.CharField(max_length=24) #번호 리스트 이름
    text = models.CharField(max_length=255) #번호 리스트 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') #번호가 담길 str
    num_lotto = models.IntegerField(default=5) #번호 set 개수
    update_date = models.DateTimeField()

    #self == 각자 열
    def generate(self):
        self.lottos = ""
        # 1~45 리스트 생성
        origin = list(range(1,46))
        #num_lotto 수만큼 for 문을 돌리고
        for _ in range(0, self.num_lotto):
            #random으로 숫자들을 뒤섞는다
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
        #현재 시간 얻어오기
        self.update_date = timezone.now()
        self.save()
    #무엇을 출력해줘야할까? print문은 당연한 것이 아님
    def __str__(self):
        #pk는 숨겨져 있다. 자동으로 반영
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
