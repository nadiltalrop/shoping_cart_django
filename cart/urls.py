from django.urls import path

from. import views

app_name = 'cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/',views.add_cart,name="add_cart"),
    path('remove/<int:product_id>/',views.minusing_cart_item,name="minusing_cart_item"),
    path('delete/<int:product_id>/',views.delete_cart_item,name='delete_cart_item'),
]