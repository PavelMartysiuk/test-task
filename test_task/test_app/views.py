from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializers import BooksSerializer
from .serializers import BookSerializer


@api_view(['GET', 'POST', ])
def get_book(request, book_id):
    """Func shows information about one book,gets information about
    new book from user  ans saves in db"""
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


@api_view(['GET', ])
def get_all_books(request):
    """Func shows all books"""
    books = Book.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)
