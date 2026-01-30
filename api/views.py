from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from django.db.models import Sum
from django.utils.dateparse import parse_date
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated


from .models import Product, Sale
from .serializers import ProductSerializer, SaleSerializer


def home(request):
    return JsonResponse({"message": "Temir Shop Backend ishlayapti!"})
#login qismi
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse(
            {"error": "Login yoki parol noto‘g‘ri"},
            status=400
        )

    login(request, user)
    return JsonResponse({"message": "Muvaffaqiyatli kirdingiz"})
#logout qismi
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Chiqildi"})



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        sana_from = self.request.query_params.get('sana_from')
        sana_to = self.request.query_params.get('sana_to')

        if sana_from and sana_to:
            queryset = queryset.filter(
                created_at__date__range=[
                    parse_date(sana_from),
                    parse_date(sana_to)
                ]
            )
        return queryset





@api_view(['GET'])
def sales_summary(request):
    sana_from = request.query_params.get('sana_from')
    sana_to = request.query_params.get('sana_to')

    sales = Sale.objects.all()

    if sana_from and sana_to:
        sales = sales.filter(
            created_at__date__range=[
                parse_date(sana_from),
                parse_date(sana_to)
            ]
        )

    total_income = sales.aggregate(
        total=Sum('total_price')
    )['total'] or 0

    return JsonResponse({
        "sana_from": sana_from,
        "sana_to": sana_to,
        "jami_kirim": total_income
    })
