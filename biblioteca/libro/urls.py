from django.urls import path 
from .views import  ( inicio ,CreateBook  , success , ListBook , updateBook , DeleteBook , 
	CreateAutor , ListAutor , updateAutor , DeleteAutor , Prestamo)

urlpatterns = [



    path('' , inicio.as_view(), name='index'),  
   
	#urls' Book
    path('create/' , CreateBook.as_view() , name='create_book'),
    path('ListBook/' , ListBook , name='list_book'),
    path('updateBook/<int:pk>' , updateBook.as_view() , name='update_book'),
    path('DeleteBook/<int:pk>' , DeleteBook.as_view() , name='delete_book'),
    path('success/' , success , name='success' ),


    #urls' Autor

    path('CreateAutor/' , CreateAutor.as_view() , name='create_autor'),
    path('ListAutor/' , ListAutor.as_view() , name='list_autor'),
    path('updateAutor/<int:pk>' , updateAutor.as_view() , name='update_autor'),
    path('DeleteAutor/<int:pk>' , DeleteAutor.as_view() , name='delete_autor'),



    # urls' prestamo


    path('Prestamo/<int:pk>' , Prestamo.as_view() , name='prestamo'),



]
 