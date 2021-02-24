from django.urls import path 
from .views import  ( inicio ,CreateBook  , success , ListBook , updateBook , DeleteBook , 
	CreateAutor , ListAutor , updateAutor , DeleteAutor , Prestamo , Create_request_Book,
    show_success_reservation , list_reservation_active , sent_email_to_user,
    list_reservation_no_active , reservation_usuario_active)

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
    path('reservacion/' , Create_request_Book.as_view() , name='reservation'),
    path('success_reservation/' , show_success_reservation.as_view() , name='success_reservation'),
    path('lista_reservacion_activa/' , list_reservation_active.as_view() , name='lista_activa'),
    path('lista_reservacion_no_activa/' , list_reservation_no_active.as_view() , name='lista__no_activa'),
    path('reservacion_usuario_activa/' , reservation_usuario_active.as_view() , name='lista__usuario_activa'),

    path('Email/<int:pk>' , sent_email_to_user.as_view() , name='Email'),



]






