from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request, 'index.html')

def add_book(request):
    
    return render(request, 'add_book.html')

def add_author(request):
    
    return render(request, 'add_author.html')