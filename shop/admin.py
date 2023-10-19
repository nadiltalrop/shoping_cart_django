from django.contrib import admin

from.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','description','image')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','description','price','category','image','stock','available','created','updated')
    list_editable = ('price','stock','available')
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product,ProductAdmin)