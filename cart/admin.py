from django.contrib import admin

from.models import *

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date_added',)
    
admin.site.register(Cart,CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product','cart','quantity','active',)

admin.site.register(CartItem,CartItemAdmin)