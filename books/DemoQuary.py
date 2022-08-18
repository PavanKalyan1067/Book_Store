# ***(1)Returns all Books from books table
books = Book.objects.all()

# (2)Returns first Book in table
first_books = Book.objects.first()

# (3)Returns last Book in table
last_books = Book.objects.last()

# (4)Returns single Book by book_title
BookByName = Book.objects.get(book_title='abcd')


# ***(5)Returns single Book by id
BookByID = Book.objects.get(id=1)

