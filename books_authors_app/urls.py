from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('author', views.author),
    path('add_author', views.add_author),
    path('get_book/<int:bookID>', views.get_book),
    path('get_book/author_to_book/<int:bookID>', views.author_to_book),
    path('get_book/delete_author/<int:bookID>/<int:authorID>', views.delete_author),
    path('get_author/<int:authorID>', views.get_author),
    path('get_author/book_to_author/<int:authorID>', views.book_to_author),
    path('get_author/delete_book/<int:authorID>/<int:bookID>', views.delete_book),
]
