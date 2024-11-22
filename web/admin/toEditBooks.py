from django.shortcuts import render


def toEditBooks(request):
    return render(request, 'admin/editBooks.html')
