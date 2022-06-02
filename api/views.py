from typing import Generic
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,status
from rest_framework.views import APIView

from api.models import *
from .serializers import *

from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.http import Http404

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
import datetime


# Below you can check additional, ways of solving the common task, one is by creating classes for each to-do the other one is using django's mixins and the third one is using the mixins
# and packing it all together in a single class with some extra logic to handle similar URL structured requests.

# - PRODUCT VIEWS - #

# - LIST VIEWS 
#Ground up
class ListProductAPIMixin(GenericAPIView,ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)

#Mixins
class ListProductsAPIView(APIView):
    def get(self,request,fomart=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# - DETAIL VIEWS
#Ground up
class DetailProductAPIView(APIView):
    def get(self,request,*args, **kwargs):
        product_id = kwargs['pk']
        try:
            product = Product.objects.get(pk = product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_404_NOT_FOUND)

#Mixins
class DetailProductAPIMixin(GenericAPIView, RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

# - CART VIEWS - #

# - LIST VIEW
#Ground up
class ViewCartAPIView(APIView):
    def get(self,request,*args,**kwargs):
        cart = CartItem.objects.all()
        serializer = CartItemSerializer(cart, many=True)
        return Response(serializer.data)

#Mixins
class ViewCartAPIViewMixin(GenericAPIView,ListModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)


# - ADD VIEWS
#Ground up
class AddProductInCartAPIView(APIView):
    def post(self,request,*args,**kwargs):
        cart_item_id = request.data.get('id')
        try:
            CartItem.objects.create(product_id=cart_item_id)
            return Response('Item with the ID:' + str(cart_item_id) + " added to cart.")
        except:
            return Response(status.HTTP_404_NOT_FOUND)

#Mixins
class AddProductInCartAPI(GenericAPIView, CreateModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)


# - REMOVE VIEWS
#Ground up
class RemoveProductInCartAPIView(APIView):
    def delete(self,request,*args,**kwargs):
        cart_item_id = kwargs['pk']
        try:
            cart_item = CartItem.objects.get(pk = cart_item_id)
            cart_item.delete()
            return Response('Item with the ID:' + str(cart_item_id) + " removed from cart.")
        except:
            return Response(status.HTTP_404_NOT_FOUND)

#Mixins
class RemoveProductInCartAPIMixin(GenericAPIView,DestroyModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class OrderCartAPIView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            date = request.data.get('delivery_date')
            datetime.datetime.strptime(date, '%Y/%m/%d %H:%M')
            cart = CartItem.objects.all()
            serializer = CartItemSerializer(cart, many=True)

            confirmation_response = list(serializer.data)
            confirmation_response.append({"delivery_date":date,"message":"Your order executed successfully"})

            cart.delete()
            return Response(confirmation_response)
        except:
            return Response('Please provide a valid delivery date - formatted: YYYY/MM/DD HH:mm')



# All packed together in a single class with multiple inheritance from Mixins.

class ListDetailProductView(ListModelMixin, RetrieveModelMixin,GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def get(self,request,*args,**kwargs):
        """ If there is a pk provided thru the URL(GET) we use the retrieve method, if not we use the list method."""
        try:
            product_id = kwargs['pk']
            return self.retrieve(request,*args,**kwargs)
        except:
            return self.list(request,*args,**kwargs)

class ListAddRemoveCartView(ListModelMixin, CreateModelMixin, DestroyModelMixin,GenericAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    def get(self,request,*args,**kwargs):
        """ List of all Cart Items."""
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        """ Add Items in Cart."""
        return self.create(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        """ Remove items from Cart."""
        return self.destroy(request,*args,**kwargs)

class PlaceOrderView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            date = request.data.get('delivery_date')
            datetime.datetime.strptime(date, '%Y/%m/%d %H:%M')
            cart = CartItem.objects.all()
            serializer = CartItemSerializer(cart, many=True)

            confirmation_response = list(serializer.data)
            confirmation_response.append({"delivery_date":date,"message":"Your order executed successfully"})

            cart.delete()
            return Response(confirmation_response)
        except:
            return Response('Please provide a valid delivery date - formatted: YYYY/MM/DD HH:mm')