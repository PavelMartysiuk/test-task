from rest_framework import serializers
from .models import Book


class BooksSerializer(serializers.ModelSerializer):
    """Serializer for one book"""
    class Meta:
        model = Book
        fields = ('id', 'title', 'author_name')


class BookSerializer(serializers.ModelSerializer):
    """Serializer for all books"""
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author_name')
