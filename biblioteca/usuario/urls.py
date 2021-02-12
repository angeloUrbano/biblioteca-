from django.urls import path 
from .views import (List_prestamo , deleteUser , updateUser , detalle_prestamo , update_estado_prestamo,
	 CreateUserANDListUser)

urlpatterns = [
    
    path('CreateUserANDListUser/' , CreateUserANDListUser.as_view() , name='CreateUserANDListUser'),
    #path('listuser/' , ListUser.as_view() , name='list_user'),
    path('deleteUser/<int:pk>' , deleteUser.as_view() , name='delete_user'),
    path('updateUser/<int:pk>' , updateUser.as_view() , name='update_user'),
   
	



    #urls de prestamo 
    path('List_prestamo/' , List_prestamo.as_view() , name='List_prestamo'),
    path('detalle_prestamo/<int:pk>' , detalle_prestamo.as_view() , name='detalle_prestamo'),
    path('update_estado_prestamo/<int:pk>' , update_estado_prestamo.as_view() , name='update_estado_prestamo'),
	

]
 