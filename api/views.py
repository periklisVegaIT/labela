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

import datetime


# PRODUCT VIEWS #
class ListProductsAPIView(APIView):
    def get(self,request,fomart=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class DetailProductAPIView(APIView):
    def get(self,request,*args, **kwargs):
        product_id = kwargs['pk']
        try:
            product = Product.objects.get(pk = product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_404_NOT_FOUND)

# CART VIEWS #
class ViewCartAPIView(APIView):
    def get(self,request,*args,**kwargs):
        cart = CartItem.objects.all()
        serializer = CartItemSerializer(cart, many=True)
        return Response(serializer.data)

class AddProductInCartAPIView(APIView):
    def post(self,request,*args,**kwargs):
        cart_item_id = request.data.get('id')
        try:
            CartItem.objects.create(product_id=cart_item_id)
            return Response('Item with the ID:' + str(cart_item_id) + " added to cart.")
        except:
            return Response(status.HTTP_404_NOT_FOUND)

class RemoveProductInCartAPIView(APIView):
    def delete(self,request,*args,**kwargs):
        cart_item_id = kwargs['pk']
        try:
            cart_item = CartItem.objects.get(pk = cart_item_id)
            cart_item.delete()
            return Response('Item with the ID:' + str(cart_item_id) + " removed from cart.")
        except:
            return Response(status.HTTP_404_NOT_FOUND)

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


