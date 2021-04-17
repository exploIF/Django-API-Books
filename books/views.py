from books_db.models import Books
from books_db import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter


class BooksListView(ListAPIView):
    """
    Class based list view of all available in database book with filter and ordering options.
    Inheriting from ListAPIView.

    Attributes
    ________
    filterset_fields : list
        is a list with all possible fields to filter by
    ordering_fields : list
        is a list with all possible fields to sort by
    queryset : queryset
        queryset with all Book's objects
    serializer_class : serializers
        serializer for Book's objects
    """

    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'title', 'author', 'publishedDate', 'category', 'averageRating', 'ratingsCount',
                        'thumbnail']
    ordering_fields = ['id', 'title', 'author', 'publishedDate', 'category', 'averageRating', 'ratingsCount']


@api_view(['GET'])
def book_detail(request, pk):
    """
    Function based view for get method. Shows detail view for one book.

    Parameters
    __________
    request: request
        request with get method
    pk: str
        Book's primary key
    """

    book = Books.objects.get(pk=pk)
    serializer = serializers.BooksSerializer(book)
    return Response(serializer.data)



