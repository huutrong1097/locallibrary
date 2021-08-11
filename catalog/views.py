from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres = Genre.objects.filter(name__icontains='a').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    # # your own name for the list as a template variable
    context_object_name = 'book_list'
    # Get 5 books containing the title war
    queryset = Book.objects.all()[:5]
    template_name = 'catalog/book_list.html'
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book



# def author_list_view(request):
#     author_list = Author.objects.all()
#     paginator = Paginator(author_list, 2)
#     page_number = request.GET.get('page', 1)
#     try:
#         authors = paginator.page(page_number)
#     except PageNotAnInteger:
#         authors = paginator.page(1)
#     except EmptyPage:
#         authors = paginator.page(paginator.num_pages)

#     return render(request, 'catalog/author_list.html', {'page_obj': authors})

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    queryset = Author.objects.all()[:5]
    template_name = 'catalog/author_list.html'
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author
    