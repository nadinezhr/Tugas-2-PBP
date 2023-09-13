from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_contains_expected_content(self): #Testing apakah tulisan ada dalam konten web
        response = Client().get('/main/')
        self.assertContains(response, 'Selamat datang di Nadterial Store')
        
