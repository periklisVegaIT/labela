from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path('',views.ListProductsAPIView.as_view()), #Lists all products in the API. 
    path('add/',views.AddProductInCartAPIView.as_view()), #Adding items to cart.
    path('remove/<int:pk>',views.RemoveProductInCartAPIView.as_view()), #Removing items from cart.
    path('cart/',views.ViewCartAPIView.as_view()), #See all products in cart
    path('product/<int:pk>',views.DetailProductAPIView.as_view()), #See detail of a product 
    path('order/',views.OrderCartAPIView.as_view()), #Order cart.

    #The urls below are for the 2 classes that contain all the methods.
    path('mixins/product/<int:pk>',views.ListDetailProductView.as_view()),
    path('mixins/products',views.ListDetailProductView.as_view()), 

    path('mixins/cart',views.ListAddRemoveCartView.as_view()),
    path('mixins/cart/<int:pk>',views.ListAddRemoveCartView.as_view()),
    path('mixins/order/',views.PlaceOrderView.as_view())

]