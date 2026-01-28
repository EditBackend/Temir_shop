from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from .models import Product, Sale
from .serializers import ProductSerializer, SaleSerializer



def home(request):
    return JsonResponse({"message": "Temir Shop Backend ishlayapti!"})




class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

