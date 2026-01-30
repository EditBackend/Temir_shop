from django.urls import path
from .views import ProductViewSet, SaleViewSet, sales_summary,  user_login,user_logout

urlpatterns = [



path('login/', user_login),
    path('logout/', user_logout),

    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path('sales-summary/', sales_summary),




    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<int:pk>/', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    path('sales/', SaleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('sales/<int:pk>/', SaleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    path('sales-summary/', sales_summary),
]

