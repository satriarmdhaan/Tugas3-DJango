from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_katalog,
        'nama': 'Muhammad Satria Ramadhan',
        'student_id': '2106751695'
    }
    return render(request, "katalog.html", context)
# TODO: Create your views here.
