from models import Book


class GetAllBooks(object):
    def process_request(self, request):
        books = Book.objects.all()
        request.session['app_books'] = books
