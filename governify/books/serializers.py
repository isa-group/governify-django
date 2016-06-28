from rest_framework import serializers
from models import Book


class BookSerializer( serializers.Serializer ):

    id = serializers.ReadOnlyField()  # read only
    title =serializers.CharField()