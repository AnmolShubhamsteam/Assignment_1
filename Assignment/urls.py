from django.contrib import admin
from django.urls import path
from greetings.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",greetings,name="greetings"),
    path("square/<int:pk>",square,name="square"),
    path("table/<int:pk>/<int:sk>", table, name="table"),
    path("sentence/<str:pk>",count_vowel,name="sentence"),
    path("book/",book_reviews,name="book")
]
