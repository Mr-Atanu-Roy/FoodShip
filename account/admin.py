from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserAddress)


# class AddressInline(admin.TabularInline):
#     model = UserAddress


# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'email', 'get_cart', 'is_staff', 'is_active', 'is_superuser')
#     list_filter = ('username', 'is_staff', 'is_active', 'is_superuser')

#     #controls fields in change page
#     fieldsets = (
#         ('PERSONAL INFORMATIONS', {'fields' : ('username', 'email', 'password', ('first_name', 'last_name'))}),
#         ('PERMISSIONS', {'fields' : ('is_staff', ('is_active', 'is_superuser'), )}),
#         ('IMPORTANT DATES', {'fields' : ('last_login', 'date_joined')}),
#         ('ADVANCED OPTIONS', {
#             'classes' : ('collapse',),
#             'fields' : ('groups', 'user_permissions')
#         }),
#     )

#     #controls fields in add pages
#     add_fieldsets = (
#         (None, {
#                 'classes' : ('wide',),
#                 'fields' : ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups')
#             }
#         ),)

#     inlines = [CartInline, DealsInline]

#     def get_cart(self, obj):
#         return obj.cart 


# # Register your models here.
# admin.site.register((Product, ProductInCart, Order))
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Cart, CartAdmin)
# admin.site.register(Deals, DealsAdmin)