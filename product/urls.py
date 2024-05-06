from .views import create_product, delete_product
from django.urls import path,include

urlpatterns = [
    path('createproduct/',create_product,name='createproduct'),
    path('deleteproduct/<str:pk>/',delete_product,name='deleteproduct')
]
