from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

books = {
    1: {
        'id': 1,
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'genre': 'Fiction',
        'published_year': 1988,
        'isbn': '9780061122415',
        'summary': 'A young shepherd named Santiago travels to Egypt after having a recurring dream of finding treasure there.',
        'user': 'aditya'
    },
    2: {
        'id': 2,
        'title': 'Harry Potter and the Sorcerer\'s Stone',
        'author': 'J.K. Rowling',
        'genre': 'Fantasy',
        'published_year': 1997,
        'isbn': '9780439708180',
        'summary': 'Harry discovers he is a wizard on his 11th birthday and attends Hogwarts School of Witchcraft and Wizardry.',
        'user': 'john'
    },
    3: {
        'id': 3,
        'title': 'Atomic Habits',
        'author': 'James Clear',
        'genre': 'Self-help',
        'published_year': 2018,
        'isbn': '9780735211292',
        'summary': 'A guide to building good habits and breaking bad ones using practical strategies.',
        'user': 'aditya'
    },
    4: {
        'id': 4,
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'published_year': 1937,
        'isbn': '9780547928227',
        'summary': 'Bilbo Baggins embarks on a journey to help dwarves reclaim their homeland from a dragon.',
        'user': 'emma'
    },
}

# View 1: Book Detail by ID
def book_detail(request, book_id):
    book = books.get(book_id)
    if not book:
        return HttpResponse("Book not found.")
    
    return HttpResponse(
        f"<h2>{book['title']}</h2>"
        f"<p><strong>Author:</strong> {book['author']}<br>"
        f"<strong>Genre:</strong> {book['genre']}<br>"
        f"<strong>Published Year:</strong> {book['published_year']}<br>"
        f"<strong>ISBN:</strong> {book['isbn']}<br>"
        f"<strong>User:</strong> {book['user']}<br>"
        f"<strong>Summary:</strong> {book['summary']}</p>"
    )

# View 2: Books by Author
def books_by_author(request, author_name):
    matched_books = [book for book in books.values() if book['author'].lower() == author_name.lower()]
    
    if not matched_books:
        return HttpResponse("No books found for this author.")
    
    response = f"<h2>Books by {author_name.title()}:</h2>"
    for book in matched_books:
        response += f"<p><strong>{book['title']}</strong> ({book['published_year']})</p>"
    
    return HttpResponse(response)

# View 3: Books by User
def books_by_user(request, user_name):
    matched_books = [book for book in books.values() if book['user'].lower() == user_name.lower()]
    
    if not matched_books:
        return HttpResponse("No books found for this user.")
    
    response = f"<h2>Books owned by {user_name.title()}:</h2>"
    for book in matched_books:
        response += f"<p><strong>{book['title']}</strong> by {book['author']}</p>"
    
    return HttpResponse(response)

def book_list(request):
    books_list = list(books.values())
    return render(request, 'book_list.html', {'books': books_list})
