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
]