from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_items_displayed_correctly(self):
        # Buat beberapa objek Item sebagai contoh
        item1 = Item.objects.create(name='Item 1', price=105)
        item2 = Item.objects.create(name='Item 2', price=23)

        # Lakukan permintaan ke halaman 'main'
        response = Client().get('/main/')

        # Periksa apakah nama dan harga item-item yang ada sesuai dengan yang diharapkan
        self.assertContains(response, item1.name)
        self.assertContains(response, item1.price)
        self.assertContains(response, item2.name)
        self.assertContains(response, item2.price)
