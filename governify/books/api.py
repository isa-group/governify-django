from rest_framework.response import Response
from rest_framework.views import APIView

from serializers import BookSerializer
from models import Book


class BookListAPI(APIView):

    def get(self, request):
        users = Book.objects.all()
        serializer = BookSerializer(users, many=True)
        serialized_users = serializer.data  # lista de diccionarios
        return Response(serialized_users)
