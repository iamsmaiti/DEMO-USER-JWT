from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item
# Create your views here.
@api_view(['GET'])
def productOverview(request):
	product_urls = {
		'List':'/item-list/',
		'Detail View':'/item-detail/<int:pk>/',
		'Create':'/item-create/',
		'Update':'/item-update/<int:pk>',
		'Delete':'/item-delete/<int:pk>/',
		}



	return Response(product_urls)
@api_view(['GET'])
def itemlist(request):
	items = Item.objects.all()
	serializer = ItemSerializer(items, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request, pk):
	items = Item.objects.get(id=pk)
	serializer = ItemSerializer(items, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
	serializer = ItemSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def itemUpdate(request, pk):
	item = Item.objects.get(id=pk)
	serializer = ItemSerializer(instance=item, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def itemDelete(request, pk):
	item = Item.objects.get(id=pk)
	item.delete()
	return Response("There's nothing! It's deleted")


