from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        author = "Author List:"
        if len(self.author.all()) == 0:
            author = "This book has no authors"
        else:
            for i in self.author.all():
                author += i.first_name + ", "
        return f"<Book Object: {self.id}, {self.title}, {self.desc}, {author}>"

    
class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(default="No notes currently")
    book = models.ManyToManyField(Books, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        book = "Book List:"
        if len(self.book.all()) == 0:
            book = "This author has no books"
        else:
            for i in self.book.all():
                book += i.title + ", "
        return f"<Author Object: {self.id}, {self.first_name}, {self.last_name}, {book}>"