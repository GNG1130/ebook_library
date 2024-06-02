from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def upload_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect('book_list')
    else:
        book_form = BookForm()
    return render(request, 'library/upload_book.html', {'book_form': book_form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    elif request.method == 'DELETE':
        book.delete()
        return redirect('book_list')
    return redirect('book_list')

def delete_all_books(request):
    if request.method == 'POST':
        Book.objects.all().delete()
        Category.objects.all().delete()
        return redirect('book_list')
    return redirect('book_list')
