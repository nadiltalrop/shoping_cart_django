from django.urls import path

from. import views

app_name = 'shop'

urlpatterns = [
    path('',views.allProCat,name='allProCat'),
    path('<slug:c_slug>/',views.allProCat,name='allProductByCat'),
    path('<slug:cat_slug>/<slug:prod_slug>',views.product_details,name="product_details"),
]