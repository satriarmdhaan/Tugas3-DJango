from django.test import TestCase, Client
from django.urls import resolve

class AppTest(TestCase):
    def app_url_html(self):
        response = Client().get('https://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def app_url_xml(self):
        response = Client().get('https://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    def app_url_json(self):
        response = Client().get('https://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code,200)