from django.urls import path 
from .views import  ( inicio ,CreateBook  , success , ListBook , updateBook , DeleteBook , 
	CreateAutor , ListAutor , updateAutor , DeleteAutor , Prestamo , Create_request_Book,
    show_success_reservation , list_reservation_active , sent_email_to_user,
    list_reservation_no_active , reservation_usuario_active)

from django.contrib.auth.decorators import login_required

urlpatterns = [



    path('' , login_required(inicio.as_view()), name='index'),  
   
	#urls' Book
    path('create/' , login_required(CreateBook.as_view()) , name='create_book'),
    path('ListBook/' , login_required(ListBook) , name='list_book'),
    path('updateBook/<int:pk>' , login_required(updateBook.as_view()) , name='update_book'),
    path('DeleteBook/<int:pk>' , login_required(DeleteBook.as_view()) , name='delete_book'),
    path('success/' , login_required(success) , name='success' ),


    #urls' Autor

    path('CreateAutor/' , login_required(CreateAutor.as_view()) , name='create_autor'),
    path('ListAutor/' , login_required(ListAutor.as_view()) , name='list_autor'),
    path('updateAutor/<int:pk>' , login_required(updateAutor.as_view()) , name='update_autor'),
    path('DeleteAutor/<int:pk>' ,login_required(DeleteAutor.as_view()) , name='delete_autor'),



    # urls' prestamo


    path('Prestamo/<int:pk>' , login_required(Prestamo.as_view()) , name='prestamo'),
    path('reservacion/' , login_required(Create_request_Book.as_view()) , name='reservation'),
    path('success_reservation/' , login_required(show_success_reservation.as_view()), name='success_reservation'),
    path('lista_reservacion_activa/' , login_required(list_reservation_active.as_view()) , name='lista_activa'),
    path('lista_reservacion_no_activa/' , login_required(list_reservation_no_active.as_view()) , name='lista__no_activa'),
    path('reservacion_usuario_activa/' , login_required(reservation_usuario_active.as_view()) , name='lista__usuario_activa'),

    path('Email/<int:pk>' , login_required(sent_email_to_user.as_view()) , name='Email'),



]






