from django.shortcuts import render
from .models import Category, Book
from .forms import BookForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    books = Book.objects.filter(published=True)
    return render(request, 'book/index.html', {
        'categories': categories,
        'books': books,
    })

def book_add(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
    return render(request, 'book/add.html', {
        'form': form
    })