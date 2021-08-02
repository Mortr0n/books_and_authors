from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors




def index(request):
    context = {
        "all_books" : Books.objects.all(),
    }
    return render(request, 'index.html', context)

def add_book(request):
    new_book = Books.objects.create(
        title=request.POST['title_input'],
        desc=request.POST['desc_input']
    )
    return redirect('/')

def author(request):
    context = {
        "all_authors" : Authors.objects.all(),
    }
    return render(request, 'author.html', context)

def add_author(request):
    new_author = Authors.objects.create(
        first_name=request.POST['first_name_input'],
        last_name=request.POST['last_name_input'],
        notes=request.POST['notes_input']
        )
    return redirect('/author')

def get_author(request, authorID):
    this_author = Authors.objects.get(id=authorID)
    
    context = {
        'this_author' : this_author,
        'all_books' : Books.objects.all()
    }
    return render(request, 'author_info.html', context)
    
def book_to_author(request, authorID):
    
    this_author = Authors.objects.get(id=authorID)
    book_to_add = request.POST['add_book_input']
    # looking to make it not add books that are already added
    # if Books.objects.filter(id=book_to_add):
    #     return redirect(f'/get_author/{authorID}')
    
    this_author.book.add(book_to_add)
    return redirect(f'/get_author/{authorID}')


    
def delete_book(request, authorID, bookID):
    # Important note!  If I want to pass the bookID as as a gettable variable I would 
    # need to either pass them all into request.session during the author page load or
    # pass it in a form using a button or something.
    if Books.objects.filter(id=bookID):
        this_author = Authors.objects.get(id=authorID)
        this_book = Books.objects.get(id=bookID)
        this_author.book.remove(this_book)
    # if you want to delete the book from the books table do the next thing
    # if Books.objects.filter(id=bookID):
    #     book_to_delete = Books.objects.get(id=bookID)
    #     book_to_delete.delete()
    return redirect(f'/get_author/{authorID}')

def delete_author(request, bookID, authorID):
    if Authors.objects.filter(id=authorID):
        this_book = Books.objects.get(id=bookID)
        this_author = Authors.objects.get(id=authorID)
        this_book.author.remove(this_author)
    return redirect(f'/get_book/{bookID}')

def get_book(request, bookID):
    this_book = Books.objects.get(id=bookID)
    all_authors = Authors.objects.all()
    # need to loop through this_book object and create a list.
    # if then create a new variable by adding only authors not in the list to it
    # author_list = []
    # for b in this_book.author:
    #     if book_to_add!= this_author.book[b]:
    #         author_list.append(this_author.book[b])
    #     else:
    #         continue
    # to do this as session I would need to pass strings that were taken individually as variables.
    context = {
        'this_book' : this_book,
        'all_authors' : all_authors
    }
    return render(request, 'book_info.html', context)

def author_to_book(request, bookID):
    this_book = Books.objects.get(id=bookID)
    author_to_add = request.POST['add_author_input']
    this_book.author.add(author_to_add)
    return redirect(f'/get_book/{bookID}')