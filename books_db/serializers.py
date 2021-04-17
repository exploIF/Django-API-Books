from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    """
    Class for serializing all fields for a Books model.
    """

    class Meta:
        model = Books
        fields = '__all__'
