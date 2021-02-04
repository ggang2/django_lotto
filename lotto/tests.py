from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate()
        print(g.update_date)
        print(g.lottos) #6개씩 5세트, 총 30개 숫자 리스트의 __str__

        self.assertTrue( len(g.lottos) > 20 ) #assert : 확인
