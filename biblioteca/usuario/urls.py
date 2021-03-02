from django.urls import path 
from .views import (List_prestamo , deleteUser , updateUser , detalle_prestamo , update_estado_prestamo,
	 CreateUserANDListUser)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('CreateUserANDListUser/' , login_required(CreateUserANDListUser.as_view()) , name='CreateUserANDListUser'),
    #path('listuser/' , ListUser.as_view() , name='list_user'),
    path('deleteUser/<int:pk>' , login_required(deleteUser.as_view()) , name='delete_user'),
    path('updateUser/<int:pk>' , login_required(updateUser.as_view()) , name='update_user'),
   
	



    #urls de prestamo 
    path('List_prestamo/' , login_required(List_prestamo.as_view()) , name='List_prestamo'),
    path('detalle_prestamo/<int:pk>' , login_required(detalle_prestamo.as_view()) , name='detalle_prestamo'),
    path('update_estado_prestamo/<int:pk>' , login_required(update_estado_prestamo.as_view()) , name='update_estado_prestamo'),
	

]
 