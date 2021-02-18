from django.urls import path 
from .views import  ( inicio ,CreateBook  , success , ListBook , updateBook , DeleteBook , 
	CreateAutor , ListAutor , updateAutor , DeleteAutor , Prestamo , Create_request_Book,
    show_success_reservation)

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




]






"""if request.method =='POST':

        form = reservationForm(request.POST)

        save_reservation = reservation()
        
        #import pdb;pdb.set_trace()

        if form.is_valid():
            
            person = Profile.objects.get(id = request.user.profile.pk)

            data= form.cleaned_data

            save_reservation.user_id= person
            save_reservation.titulo_libro= data['titulo_libro']
            save_reservation.autor_libro= data['autor_libro']
            save_reservation.cantidad_solicitada= data['cantidad_solicitada']
            save_reservation.descripcion= data['descripcion']

            save_reservation.save()

            return redirect('libro:success_reservation')
    else:
        form= reservationForm()
         
    print(form.errors)
    return render(request , 'usuario_template/reservation.html' , {'form':form })"""
 