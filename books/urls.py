from django.urls import path
from .views import book_detail, BooksListView


urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<str:pk>', book_detail, name='book_detail')
]