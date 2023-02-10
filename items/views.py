# from rest_framework.response import Response
# from rest_framework.generics import get_object_or_404
# from django.http import Http404
# from rest_framework import status
# from rest_framework.views import APIView
# from .models import Item
# from .serializers import ItemSerializer



# class ItemsListView(APIView):
#     def get(self,request,format = None):
#         item = Item.objects.all()
#         serializer =ItemSerializer(item,many = True)
#         return Response({"items": serializer.data})

#     def post(self,request,format= None):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class ItemsDetailView(APIView):
#     def get_object(self,pk):
#         try:
#             return Item.objects.get(pk=pk)
#         except Item.DoesNotExist:
#             raise Http404
            
#     def get(self,request,pk):
#         item = self.get_object(pk)
#         serializer = ItemSerializer(item)
#         return Response (serializer.data)

#     def put(self, request, pk):
#         saved_item = get_object_or_404(Item.objects.all(), pk=pk)
#         data = request.data.get('items')
#         serializer = ItemSerializer(instance=saved_item, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             item_saved = serializer.save()
#         return Response({
#             "success": "Item '{}' updated successfully".format(item_saved.name)
#         })
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk ):
#         item = get_object_or_404(Item.objects.all(), pk=pk)
#         item.delete()
#         return Response({
#             "message": "Item with id `{}` has been deleted.".format(pk)
#         },  status=204)


from django.shortcuts import render
from django.urls.conf import include 
from . serializers import ItemSerializer
from . models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer