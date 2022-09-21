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
```
INSTALLED_APPS = [
  ...,
  'mywatchlist',
]
```

3. Buka 'urls.py' di folder `project_django` dan tambahkan path `mywatchlist` seperti sebagai berikut.
```
urlpatterns = [
  ...,
   path('mywatchlist/', include('mywatchlist.urls')),
]
```

4. Buka file `models.py` yang ada pada folder `mywatchlist` dan menambahkan potongan kode berikut.
```
from django.db import models

class watchlist(models.Model):
    title = models.CharField(max_length=255)
    watched = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
```

5. Jalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam _database_ Django lokal.

6. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam _database_ Django lokal.

7. Buatlah sebuah folder bernama `fixtures` di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `initial_mywatchlist_data.json` yang berisi kode berikut.
```
[
    {
        "model": "mywatchlist.watchlist",
        "pk": 1,
        "fields": {
            "title": "House Of The Dragons",
            "watched": "Sudah",
            "rating": 5,
            "release_date": "10 September 2022",
            "review": "Filmnya bagus dan memiliki alur cerita yang menarik."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 2,
        "fields": {
            "title": "Mencuri Raden Saleh",
            "watched": "Belum",
            "rating": 4,
            "release_date": "15 September 2022",
            "review": "Filmnya memiliki alur cerita yang menarik dan menegangkan."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 3,
        "fields": {
            "title": "SPY x FAMILY",
            "watched": "Belum",
            "rating": 5,
            "release_date": "9 April 2022",
            "review": "Filmnya bagus dan ramah ditonton bersama keluarga."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 4,
        "fields": {
            "title": "Kimi No Nawa(Your Name)",
            "watched": "Sudah",
            "rating": 5,
            "release_date": "26 Agustus 2016",
            "review": "Memiliki alur cerita yang kompleks dan menyentuh hati."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 5,
        "fields": {
            "title": "Avengers: Endgame",
            "watched": "Sudah",
            "rating": 5,
            "release_date": "24 April 2019",
            "review": "CGI nya bagus dan filmnya tidak membosankan."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 6,
        "fields": {
            "title": "Top Gun: Maverick",
            "watched": "Sudah",
            "rating": 5,
            "release_date": "24 Mei 2022",
            "review": "Pembuatan filmnya totalitas karena banyak stunt yang dilakukan secara nyata."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 7,
        "fields": {
            "title": "No Time To Die",
            "watched": "Sudah",
            "rating": 4,
            "release_date": "29 September 2021",
            "review": "Filmnya menegangkan dan hanyut akan emosi."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 8,
        "fields": {
            "title": "Incantation",
            "watched": "Sudah",
            "rating": 5,
            "release_date": "18 Maret 2022",
            "review": "Filmnya seram dan mengerikan dengan konsep film documentary."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 9,
        "fields": {
            "title": "Stranger Things",
            "watched": "Belum",
            "rating": 5,
            "release_date": "15 Juli 2016",
            "review": "Plot ceritanya bagus dan memunculkan rasa penasaran."
        }
    },
    {
        "model": "mywatchlist.watchlist",
        "pk": 10,
        "fields": {
            "title": "Thor: Love and Thunder",
            "watched": "Belum",
            "rating": 3,
            "release_date": "06 Juli 2022",
            "review": "Filmnya kurang menarik dan tidak menggambarkan film-film dari Marvel."
        }
    }
]
```
## Postman
# HTML
![mywatchlist-html](https://user-images.githubusercontent.com/112569195/191591557-9c07f489-9013-4e14-9688-bc39b70b3a14.jpg)

# JSON
![mywatchlist-json](https://user-images.githubusercontent.com/112569195/191591672-e13a98c4-6f08-441c-8484-e33b0fa9179e.jpg)

# XML
![mywatchlist-xml](https://user-images.githubusercontent.com/112569195/191591702-574dee67-ef10-4e17-a5c9-928cff92a478.jpg)
