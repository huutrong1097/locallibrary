from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('books/', views.book_list, name='book_list'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail')
    # path('books/<id>/', views.book_detail, name='book_detail'),
]