from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View

from models import Book

class inicio(View):


    def get(self,request):
        books = Book.objects.all()
        context ={
            'app_books': books
        }

        return render(request,'books/example.html',context)