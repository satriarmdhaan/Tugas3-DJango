## Link HEROKUAPP

Link : [Link](https://tugas3-django.herokuapp.com/mywatchlist/)

## Perbedaan antara JSON, XML, dan HTML
- JSON : JSON (JavaScript Object Notation) adalah suatu format dari JavaScript untuk menyimpan dan mentransfer data dalam bentuk key dan value dengan format array.
- XML  : XML (eXtensible Markup Language) adalah markup language seperti HTML yang berguna untuk menyimpan dan mentransfer data dalam bentuk teks sederhana dengan tree seperti HTML.
- HTML : HTML (HyperText Markup Language) adalah markup language yang paling umum digunakan untuk membuat suatu laman website. Dalam HTML anda bisa membuat struktur tampilan laman website anda sendiri. HTMl digunakan hanya untuk menampilkan data-data dari bahasa pemrograman menjadi suatu tampilan yang lebih dimengerti oleh orang awam dan bukan untuk mentransfer data.

## Data Delivery dalam Implementasi Platform

## Langkah - Langkah Implementasi
1. Membuat `django-app` bernama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`.
2. Buka `settings.py` di folder `project_django` dan tambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan `django-app` yang sudah dibuat.
```shell
  INSTALLED_APPS = [
    ...,
    'mywatchlist',
  ]
```
3. Buka file `models.py` yang ada pada folder `mywatchlist` dan menambahkan potongan kode berikut.
```shell
from django.db import models

class watchlist(models.Model):
    title = models.CharField(max_length=255)
    watched = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
```

## Postman
# HTML
![mywatchlist-html](https://user-images.githubusercontent.com/112569195/191591557-9c07f489-9013-4e14-9688-bc39b70b3a14.jpg)

# JSON
![mywatchlist-json](https://user-images.githubusercontent.com/112569195/191591672-e13a98c4-6f08-441c-8484-e33b0fa9179e.jpg)

# XML
![mywatchlist-xml](https://user-images.githubusercontent.com/112569195/191591702-574dee67-ef10-4e17-a5c9-928cff92a478.jpg)
