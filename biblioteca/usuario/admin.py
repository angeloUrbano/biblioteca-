from django.contrib import admin
from usuario.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

	list_display=('user' , 'phone_number' )
	list_display_links=('user' , 'phone_number')
	search_fields=('user__username','user__email' , 'user_first_name' , 'user_last_name' , 'user_phone_number')


	fieldsets=(
		('Profile', {
			'fields':(('user' , 'picture'),),
			}),

		('Extra Info' , {'fields': ('website' , 'phone_number' , 'biography')}),

		('Meda Dato', {

			'fields':('create' , 'modified'), 
		})




		)

	""" 
		esto variable readonly_fields es por que el create y modife 
		no es una variable que se pueda editar y me da error 
		entonces para hace rque se muestre hay que hacer... lo que hice solo para mostrarlo 
		solo para leerrr
	"""
	readonly_fields=('create' , 'modified', 'user')


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
admin.site.unregister(User)
admin.site.register(User,UserAdmin)  