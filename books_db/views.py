from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Books, Authors, Categories
from rest_framework import status


@api_view(['POST'])
def db_insertion(request):
    """
    Function based view for post method. Inserting data from google books api to database.

    Parameters
    _________
    request : request
        Request with post method and body with 'q' key. Value of 'q' is a query to search in google api books.
    Returns response 200 if book record was updated or created, else returns 400 response.
    """
    try:
        query = request.data['q']
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST) # if request body doesn't have 'q'
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + query)
    if response.status_code == 200:
        data = response.json()
        fields = ('thumbnail', 'authors', 'categories', 'averageRating', 'ratingsCount', 'publishedDate', 'title')
        for element in data['items']:
            book_data = element['volumeInfo']
            if element['id'] not in Books.objects.values_list('id', flat=True).distinct():
                new_book = Books(id=element['id'])  # adding book object to database if book with this id is not in db
                new_book.save()
            else:
                new_book = Books.objects.get(id=element['id'])  # getting book if book with this id is in database
            for field in fields:
                try:
                    if field == 'thumbnail':
                        new_book.thumbnail = book_data['imageLinks']['thumbnail']
                    elif field == 'authors':
                        for single_author in book_data['authors']:
                            try:
                                current_author = Authors.objects.get(name=single_author)
                            except Authors.DoesNotExist:
                                current_author = Authors(name=single_author)    # if author doesn't exist creating it
                                current_author.save()
                            new_book.author.add(current_author)
                    elif field == 'categories':
                        for category in book_data['categories']:
                            try:
                                current_category = Categories.objects.get(name=category)
                            except Categories.DoesNotExist:
                                current_category = Categories(name=category)    # if category doesn't exist creating it
                                current_category.save()
                            new_book.category.add(current_category)
                    else:
                        setattr(new_book, field, book_data[field])
                except KeyError:
                    pass
            new_book.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


