# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import ItemsListView, ItemsDetailView

# app_name = "items"

# urlpatterns = [
#     path('items/',ItemsListView.as_view()),
#     path('items/<int:pk>/',ItemsDetailView.as_view())
# ]

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . views import *



urlpatterns = [
    path('items/', ItemList.as_view()),
    path('items/<int:pk>', ItemDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)