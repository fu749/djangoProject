from django.shortcuts import render

from function2.searchBook import searchBook_id, addBook_id


def editBooks(request):
    book_id = request.GET.get('id')
    books = searchBook_id(book_id)
    books_data = {
            'bookId': books[0],
            'bookName': books[1],
            'author': books[2],
            'bookNum': books[3]
        }
    return render(request, 'admin/bookInfo.html',books_data)



def addBooks(request):
    bid = addBook_id()
    books_data = {
        'bookId': bid,
        'bookName': "",
        'author': "",
        'bookNum': ""
    }
    return render(request, 'admin/bookInfo.html',books_data)