from django.contrib import admin

# Register your models here.admin.site.register(Publication)
from models import Book, Author, Publisher

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
